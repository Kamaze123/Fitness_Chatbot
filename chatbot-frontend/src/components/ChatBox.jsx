import { useState, useEffect, useRef } from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

function ChatBox() {
  const [messages, setMessages] = useState([]);
  const bottomRef = useRef(null);
  const hasMessages = messages.length > 0;

  const sendMessage = async (text) => {
    setMessages((prev) => [...prev, { text, sender: "user" }]);
    
    try {

    const res = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message: text
      })
    });

    const data = await res.json();

    // add bot reply
    setMessages((prev) => [
      ...prev,
      { text: data.response, sender: "bot" }
    ]);

  } catch (error) {
    console.error(error);

    setMessages((prev) => [
      ...prev,
      { text: "Something went wrong connecting to the server.", sender: "bot" }
    ]);
  }

  };

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="flex flex-col h-[100dvh] bg-black text-white overflow-hidden">

      {/* Message area — animates via max-height */}
      <div
        style={{
          maxHeight: hasMessages ? "100vh" : "0px",
          opacity: hasMessages ? 1 : 0,
          transition: "max-height 600ms ease-in-out, opacity 400ms ease-in-out",
          overflowY: hasMessages ? "auto" : "hidden",
          flex: hasMessages ? "1 1 0" : "0 0 0",
        }}
        className="custom-scroll"
      >
        <div className="max-w-2xl mx-auto w-full px-4 py-6">
          {messages.map((msg, i) => (
            <MessageBubble key={i} message={msg.text} sender={msg.sender} />
          ))}
          <div ref={bottomRef} />
        </div>
      </div>

      {/* Hero + Input */}
      <div
        style={{
          transition: "flex 600ms ease-in-out, justify-content 600ms ease-in-out",
        }}
        className={`flex flex-col items-center px-4
          ${hasMessages ? "justify-end pb-6 sm:pb-8" : "flex-1 justify-center gap-6"}`}
      >
        {/* Hero text — collapses smoothly */}
        <div
          style={{
            maxHeight: hasMessages ? "0px" : "200px",
            opacity: hasMessages ? 0 : 1,
            overflow: "hidden",
            transition: "max-height 500ms ease-in-out, opacity 300ms ease-in-out",
            marginBottom: hasMessages ? "0px" : undefined,
          }}
          className="text-center"
        >
          <p className="text-lg sm:text-xl md:text-2xl text-white font-light tracking-wide pb-1">
            Hello I am{" "}
            <span className="text-blue-400 font-semibold">FitBuddy</span>
          </p>
          <p className="text-lg sm:text-xl md:text-2xl text-white font-light mt-1 pb-4">
            Your AI fitness coach
          </p>
        </div>

        {/* Input box */}
        <div
          style={{
            width: "100%",
            maxWidth: hasMessages ? "672px" : "560px",
            transition: "max-width 500ms ease-in-out",
          }}
        >
          <ChatInput sendMessage={sendMessage} />
        </div>
      </div>

    </div>
  );
}

export default ChatBox;