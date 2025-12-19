'use client';

export default function Home() {
  async function createGame(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const response = await fetch("http://localhost:8000/start-game", {
      method: "POST",
    });
  }

  const messages = [
    { role: "system", text: "You are standing in an open field west of a white house, with a boarded front door. There is a small mailbox here." },
    { role: "user", text: "I open the mailbox" },
  ];

  const messageViews = messages.map((message, index) => (
    <div key={index} className="border border-gray-200 rounded-md p-6 bg-white shadow mb-4">
      {message.text}
    </div>
  ));

  return (
    <div className="flex flex-col h-screen max-w-4xl mx-auto p-12">
      <div className="flex-1 overflow-y-auto">
        {messageViews}
      </div>
      <form className="flex" onSubmit={createGame}>
        <textarea
          className="flex-1 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none overflow-hidden border border-gray-400 rounded-md p-4 mr-4"
          placeholder="Describe an action of your character..."
          rows={3}
        ></textarea>
        <button type="submit" className="p-4 font-bold bg-gray-100 hover:bg-gray-200 active:bg-gray-300 text-gray-700 active:text-gray-800 border border-gray-400 active:border-gray-500 rounded-md">Enter</button>
      </form>
    </div>
  );
}
