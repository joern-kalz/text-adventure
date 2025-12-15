import Image from "next/image";
import React from "react";

export default function Home() {
  return (
    <div className="flex flex-col h-screen max-w-4xl mx-auto p-12">
      <div className="flex-1 overflow-y-auto space-y-4">
        <div className="border border-gray-200 rounded-2xl p-6 bg-white shadow">
          You are standing in an open field west of a white house, with a boarded
          front door. There is a small mailbox here.
        </div>
        <div className="border border-gray-200 rounded-2xl p-6 bg-white shadow">
          I open the mailbox.
        </div>
      </div>
      <form className="flex">
        <textarea
          className="flex-1 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none overflow-hidden"
          placeholder="Enter an action of your character..."
          rows={3}
        ></textarea>
        <input type="button" value="Send" className="" />
      </form>
    </div>
  );
}
