"use client";

import React, { useState } from "react";
import KeyButton from "./KeyButton";

interface MessageFormProps {
    onPerformAction: (action: string) => Promise<void>;
    onPause: () => Promise<void>;
}

export default function MessageForm({ onPerformAction, onPause }: MessageFormProps) {
    const [disabled, setDisabled] = useState(false);
    const [inputValue, setInputValue] = useState("");

    async function handleInput(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault();
        setDisabled(true);
        await onPerformAction(inputValue);
        setDisabled(false);
        setInputValue("");
    }

    return (
        <form className="flex" onSubmit={handleInput}>
            <input
                className="flex-1 focus:outline-none focus:ring-2 focus:ring-gray-100 resize-none overflow-hidden border border-gray-400 rounded-md p-4"
                placeholder="Describe an action of your character..."
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                disabled={disabled}
            ></input>
            <KeyButton
                type="submit"
                disabled={disabled}
            >Enter</KeyButton>
            <KeyButton
                type="button"
                disabled={disabled}
                onClick={onPause}
            >Esc</KeyButton>
        </form>
    );
}