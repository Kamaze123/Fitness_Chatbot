import ReactMarkdown from "react-markdown";

function MessageBubble({ message, sender }) {
  const isUser = sender === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-3`}>
      <div
        className={`px-4 py-2.5 rounded-2xl max-w-[85%] sm:max-w-[70%] md:max-w-[60%]
          text-sm sm:text-base leading-relaxed
          ${isUser ? "bg-blue-600 text-white" : "bg-zinc-800 text-zinc-100"}`}
      >
        {isUser ? (message) :(
            <ReactMarkdown
                components={{
              p: ({ children }) => <p className="mb-2 last:mb-0">{children}</p>,
              strong: ({ children }) => <strong className="font-semibold text-white">{children}</strong>,
              ul: ({ children }) => <ul className="list-disc list-inside space-y-1 mb-2">{children}</ul>,
              ol: ({ children }) => <ol className="list-decimal list-inside space-y-1 mb-2">{children}</ol>,
              li: ({ children }) => <li className="text-zinc-100">{children}</li>,
            }}
            >
                {message}
            </ReactMarkdown>
        )}
      </div>
    </div>
  );
}

export default MessageBubble;