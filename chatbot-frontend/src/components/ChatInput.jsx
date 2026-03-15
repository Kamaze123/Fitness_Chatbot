import { useState } from "react";

function ChatInput({ sendMessage }) {
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    sendMessage(input);
    setInput("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") handleSend();
  };

  return (
    <div className="flex items-center gap-2 bg-zinc-800 p-2 sm:p-3 rounded-xl border border-zinc-700 focus-within:border-zinc-500 transition-colors">
      <input
        className="flex-1 bg-transparent outline-none text-sm sm:text-base text-white placeholder-zinc-500 px-2"
        placeholder="Ask FitBuddy..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
      />
      <button
        className="bg-blue-500 hover:bg-blue-600 active:scale-95 transition-all px-3 py-2 sm:px-4 sm:py-2 rounded-lg text-sm sm:text-base font-medium shrink-0"
        onClick={handleSend}
      >
        Send
      </button>
    </div>
  );
}

export default ChatInput;