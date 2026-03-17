import { useCallback, useState } from "react";

import { streamChat } from "@/services/api";

type Message = { role: "user" | "assistant"; content: string };
type Source = { file_path: string; text: string };

export function useStreamingChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [sources, setSources] = useState<Record<number, Source[]>>({});
  const [isLoading, setIsLoading] = useState(false);

  const sendMessage = useCallback(async (message: string, pipeline: string) => {
    let assistantIndex = -1;
    setMessages((prev) => {
      assistantIndex = prev.length + 1;
      return [...prev, { role: "user", content: message }, { role: "assistant", content: "" }];
    });
    setIsLoading(true);
    let response = "";

    try {
      for await (const event of streamChat(message, pipeline)) {
        if (event.type === "token") {
          response += event.data;
          setMessages((prev) => {
            const updated = [...prev];
            updated[updated.length - 1] = { role: "assistant", content: response };
            return updated;
          });
        }
        if (event.type === "sources") {
          setSources((prev) => ({ ...prev, [assistantIndex]: event.data }));
        }
      }
    } finally {
      setIsLoading(false);
    }
  }, []);

  return { messages, sources, isLoading, sendMessage };
}
