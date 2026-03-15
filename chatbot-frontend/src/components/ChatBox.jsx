import { useState, useEffect, useRef } from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

function ChatBox() {
  const [messages, setMessages] = useState([]);
  const bottomRef = useRef(null);
  const hasMessages = messages.length > 0;

  const sendMessage = (text) => {
    setMessages((prev) => [...prev, { text, sender: "user" }]);
    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        { text: "Got it! Let me help you with that 💪", sender: "bot" },
      ]);
    }, 800);
  };

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="flex flex-col h-[100dvh] bg-zinc-900 text-white overflow-hidden">

      {/* TOP SECTION — expands to push input down once chat starts */}
      <div className={`flex flex-col transition-all duration-500 ease-in-out
        ${hasMessages ? "flex-1 overflow-y-auto" : "flex-none h-0"}`}
      >
        <div className="px-3 sm:px-6 md:px-8 py-4 sm:py-6 max-w-2xl mx-auto w-full">
          {messages.map((msg, i) => (
            <MessageBubble key={i} message={msg.text} sender={msg.sender} />
          ))}
          <div ref={bottomRef} />
        </div>
      </div>

      {/* BOTTOM SECTION — always in flow, vertically centered when no messages */}
      <div className={`flex flex-col items-center justify-center transition-all duration-500 ease-in-out px-3 sm:px-6 md:px-8
        ${hasMessages ? "pb-4 sm:pb-6 justify-end" : "flex-1 justify-center"}`}
      >
        {/* Hero text — fades out when chat starts */}
        <div className={`text-center mb-5 transition-all duration-400 ease-in-out
          ${hasMessages ? "opacity-0 h-0 mb-0 overflow-hidden" : "opacity-100"}`}
        >
          <h1 className="text-xl sm:text-2xl md:text-3xl font-semibold text-zinc-300 tracking-tight">
            What's your goal today?
          </h1>
          <p className="text-zinc-500 text-sm sm:text-base mt-2">
            Your AI fitness companion is ready
          </p>
        </div>

        {/* Input box */}
        <div className={`w-full transition-all duration-500 ease-in-out
          ${hasMessages ? "max-w-2xl" : "max-w-xs sm:max-w-md md:max-w-xl"}`}
        >
          <ChatInput sendMessage={sendMessage} />
        </div>
      </div>

    </div>
  );
}

export default ChatBox;