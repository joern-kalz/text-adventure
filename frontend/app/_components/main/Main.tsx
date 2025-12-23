"use client";

import { Overview } from "@/app/_components/_dto/Overview";
import { Step } from "@/app/_components/_dto/Step";
import MessageForm from "./MessageForm";
import Messages from "./Messages";

interface MainProps {
    overview: Overview;
    steps: Step[];
    onPerformAction: (action: string) => Promise<void>;
    onPause: () => Promise<void>;
}

export default function Main({ overview, steps, onPerformAction, onPause }: MainProps) {
    return (
        <div className="flex flex-col h-full w-full">
            <Messages overview={overview} steps={steps} />
            <MessageForm onPerformAction={onPerformAction} onPause={onPause} />
        </div>
    );
}
