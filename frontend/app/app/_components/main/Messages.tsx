import { Overview } from "@/app/_components/_dto/Overview";
import { Step } from "@/app/_components/_dto/Step";
import React, { useEffect } from "react";
import { useRef } from 'react';

interface MessagesProps {
    overview: Overview;
    steps: Step[];
}

export default function Messages({ overview, steps }: MessagesProps) {
    const messagesList = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (messagesList.current) {
            messagesList.current.scrollTop = messagesList.current.scrollHeight;
        }
    }, [steps]);

    const stepViews = steps.map((step, index) => (
        <React.Fragment key={index}>
            <div className="mb-4">
                &gt; {step.action}
            </div>
            {step.result && <div className="mb-4">
                {step.result.outcome}
            </div>}
        </React.Fragment>
    ));

    return (
        <div className="flex-1 overflow-y-auto" ref={messagesList}>
            <div className="mb-4">
                {overview.beginning}
            </div>
            {stepViews}
        </div>
    );
}