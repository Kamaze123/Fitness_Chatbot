function MessageBubble({ message, sender }) {
  const isUser = sender === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-3`}>
      <div
        className={`px-3 py-2 sm:px-4 sm:py-2 rounded-xl 
          max-w-[85%] sm:max-w-[70%] md:max-w-[60%] lg:max-w-[50%] 
          text-sm sm:text-base leading-relaxed
          ${isUser ? "bg-blue-500" : "bg-zinc-700"}`}
      >
        {message}
      </div>
    </div>
  );
}

export default MessageBubble;