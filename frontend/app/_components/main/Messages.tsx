import { Overview } from "@/app/_components/_dto/Overview";
import { Step } from "@/app/_components/_dto/Step";
import React from "react";

interface MessagesProps {
    overview: Overview;
    steps: Step[];
}

export default function Messages({ overview, steps }: MessagesProps) {
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
        <div className="flex-1 overflow-y-auto">
            <div className="mb-4">
                {overview.beginning}
            </div>
            {stepViews}
        </div>
    );
}