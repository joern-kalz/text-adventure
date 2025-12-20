"use client";

import { Overview } from "@/app/_components/_dto/Overview";
import { Step } from "@/app/_components/_dto/Step";
import React, { useState } from "react";

interface MainProps {
    overview: Overview;
    steps: Step[];
    onPerformAction: (action: string) => Promise<void>;
}

type State = "waiting_for_user" | "waiting_for_server";

export default function Main({ overview, steps, onPerformAction }: MainProps) {
    const [state, setState] = useState<State>("waiting_for_user");
    const [inputValue, setInputValue] = useState("");

    async function handleInput(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault();
        setState("waiting_for_server");
        await onPerformAction(inputValue);
        setState("waiting_for_user");
        setInputValue("");
    }

    const stepViews = steps.map((step, index) => (
        <React.Fragment key={index}>
            <div key={index} className="border border-gray-200 rounded-md p-6 bg-white shadow mb-4">
                {step.action}
            </div>
            <div key={index} className="border border-gray-200 rounded-md p-6 bg-white shadow mb-4">
                {step.action}
            </div>
        </React.Fragment>
    ));

    return (
        <div className="flex flex-col h-full w-full">
            <div className="flex-1 overflow-y-auto">
                <div className="border border-gray-200 rounded-md p-6 bg-white shadow mb-4">
                    {overview.beginning}
                </div>
                {stepViews}
            </div>
            <form className="flex" onSubmit={handleInput}>
                <input
                    className="flex-1 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none overflow-hidden border border-gray-400 rounded-md p-4 mr-4"
                    placeholder="Describe an action of your character..."
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    disabled={state === "waiting_for_server"}
                ></input>
                <button
                    type="submit"
                    className="p-4 font-bold bg-gray-100 hover:bg-gray-200 active:bg-gray-300 text-gray-700 active:text-gray-800 border border-gray-400 active:border-gray-500 rounded-md"
                    disabled={state === "waiting_for_server"}
                >Enter</button>
            </form>
        </div>
    );
}
