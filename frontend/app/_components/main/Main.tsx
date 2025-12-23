"use client";

import { Overview } from "@/app/_components/_dto/Overview";
import { Step } from "@/app/_components/_dto/Step";
import React, { useState } from "react";
import KeyButton from "./KeyButton";
import Steps from "./Steps";

interface MainProps {
    overview: Overview;
    steps: Step[];
    onPerformAction: (action: string) => Promise<void>;
    onPause: () => Promise<void>;
}

type State = "waiting_for_user" | "waiting_for_server";

export default function Main({ overview, steps, onPerformAction, onPause }: MainProps) {
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
        <div className="flex flex-col h-full w-full">
            <Steps overview={overview} steps={steps} />
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
        </div>
    );
}
