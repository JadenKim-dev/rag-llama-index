import { useState } from "react";

import { SourcePanel } from "@/components/chat/SourcePanel";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { useStreamingChat } from "@/hooks/useStreamingChat";

export function ChatSection() {
  const [input, setInput] = useState("");
  const [pipeline, setPipeline] = useState("basic");
  const { messages, sources, isLoading, sendMessage } = useStreamingChat();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) {
      return;
    }
    void sendMessage(input.trim(), pipeline);
    setInput("");
  };

  return (
    <div className="flex flex-col h-screen max-w-3xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Code RAG Lab</h1>
      <select
        className="mb-4 p-4 border rounded"
        value={pipeline}
        onChange={(e) => setPipeline(e.target.value)}
      >
        <option value="basic">Basic Vector Search</option>
      </select>
      <ScrollArea className="flex-1 border rounded p-4 mb-4">
        {messages.map((msg, i) => (
          <div key={`${msg.role}-${i}`} className={`mb-4 ${msg.role === "user" ? "text-right" : "text-left"}`}>
            <span
              className={`inline-block px-3 py-2 rounded-lg text-sm whitespace-pre-wrap max-w-[80%] ${
                msg.role === "user" ? "bg-blue-500 text-white" : "bg-gray-100"
              }`}
            >
              {msg.content}
            </span>
            {msg.role === "assistant" && sources[i]?.length ? <SourcePanel sources={sources[i]} /> : null}
          </div>
        ))}
        {isLoading ? <div className="text-gray-400 text-sm">응답 생성 중...</div> : null}
      </ScrollArea>
      <form onSubmit={handleSubmit} className="flex gap-2">
        <Input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="코드에 대해 질문하세요..."
          disabled={isLoading}
        />
        <Button type="submit" disabled={isLoading || !input.trim()}>
          전송
        </Button>
      </form>
    </div>
  );
}
