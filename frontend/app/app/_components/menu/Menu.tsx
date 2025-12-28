"use client";

import ActionButton from "./ActionButton";

export interface MenuProps {
    onStartGame: () => Promise<void>;
    onResumeGame: () => Promise<void>;
    canResumeGame: boolean;
}

export default function Menu({ onStartGame, onResumeGame, canResumeGame }: MenuProps) {
    return (
        <div className="flex flex-col justify-center items-center h-full w-full">
            <ActionButton onClick={onStartGame} text="Start Game" />
            <ActionButton onClick={onResumeGame} text="Resume Game" disabled={!canResumeGame} />
        </div>
    );
}
