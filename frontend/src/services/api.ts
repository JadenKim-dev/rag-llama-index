const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

export type StreamEvent =
  | { type: "token"; data: string }
  | { type: "sources"; data: { file_path: string; text: string }[] };

export async function* streamChat(message: string, pipeline: string): AsyncGenerator<StreamEvent> {
  const resp = await fetch(`${API_URL}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, pipeline }),
  });

  if (!resp.ok || !resp.body) {
    throw new Error(`HTTP ${resp.status}`);
  }

  const reader = resp.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    buffer += decoder.decode(value ?? new Uint8Array(), { stream: !done });
    const chunks = buffer.split("\n\n");
    buffer = chunks.pop() ?? "";

    for (const chunk of chunks) {
      let eventType = "message";
      for (const line of chunk.split("\n")) {
        if (line.startsWith("event: ")) {
          eventType = line.slice(7);
        }
        if (line.startsWith("data: ")) {
          const data = line.slice(6);
          if (eventType === "token" || eventType === "message") {
            yield { type: "token", data };
          }
          if (eventType === "sources") {
            yield { type: "sources", data: JSON.parse(data) };
          }
          if (eventType === "done") {
            return;
          }
        }
      }
    }

    if (done) {
      break;
    }
  }
}
