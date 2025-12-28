'use client';

import { useTransition } from "react";
import LoadingSpinner from "./LoadingSpinner";

export interface ActionButtonProps {
    text: string;
    onClick: () => void | Promise<void>;
    disabled?: boolean;
}

export default function ActionButton({ text, onClick, disabled }: ActionButtonProps) {
    const [isPending, startTransition] = useTransition();

    function handleClick(event: React.MouseEvent<HTMLButtonElement>) {
        startTransition(async () => {
            await onClick();
        });
    }

    return (
        <button onClick={handleClick} disabled={isPending || disabled} className="relative p-4 bg-gray-100 hover:bg-gray-200 active:bg-gray-300 text-gray-700 active:text-gray-800 border border-gray-400 active:border-gray-500 rounded-md w-50 m-3 cursor-pointer disabled:bg-gray-100 disabled:text-gray-400 disabled:border-gray-400 disabled:cursor-default">
            <span className={isPending ? "opacity-50" : ""}>{text}</span>
            {isPending && <LoadingSpinner />}
        </button>
    );
}