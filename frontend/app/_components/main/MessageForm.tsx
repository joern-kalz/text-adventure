"use client";

import React, { useState } from "react";
import KeyButton from "./KeyButton";

interface MessageFormProps {
    onPerformAction: (action: string) => Promise<void>;
    onPause: () => Promise<void>;
}

type State = "waiting_for_user" | "waiting_for_server";

export default function MessageForm({ onPerformAction, onPause }: MessageFormProps) {
    const [state, setState] = useState<State>("waiting_for_user");
    const [inputValue, setInputValue] = useState("");

    async function handleInput(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault();
        setState("waiting_for_server");
        await onPerformAction(inputValue);
        setState("waiting_for_user");
        setInputValue("");
    }

    return (
        <form className="flex" onSubmit={handleInput}>
            <input
                className="flex-1 focus:outline-none focus:ring-2 focus:ring-gray-100 resize-none overflow-hidden border border-gray-400 rounded-md p-4"
                placeholder="Describe an action of your character..."
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                disabled={state === "waiting_for_server"}
            ></input>
            <KeyButton
                type="submit"
                disabled={state === "waiting_for_server"}
            >Enter</KeyButton>
            <KeyButton
                type="button"
                disabled={state === "waiting_for_server"}
                onClick={onPause}
            >Esc</KeyButton>
        </form>
    );
}