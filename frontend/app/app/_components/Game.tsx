"use client";

import { sendPerformAction } from "@/libs/sendPerformAction";
import { sendStartGame } from "@/libs/sendStartGame";
import { useState } from "react";
import { Overview } from "./_dto/Overview";
import { Step } from "./_dto/Step";
import Main from "./main/Main";
import Menu from "./menu/Menu";

export default function Game() {
  const [overview, setOverview] = useState<Overview>();
  const [steps, setSteps] = useState<Step[]>([]);
  const [paused, setPaused] = useState<boolean>(false);

  async function startGame() {
    setSteps([]);
    setOverview(undefined);
    const response = await sendStartGame();
    setOverview(response);
    setPaused(false);
  }

  async function pauseGame() {
    setPaused(true);
  }

  async function resumeGame() {
    setPaused(false);
  }

  async function performAction(action: string, session_token: string) {
    const oldSteps = steps;
    setSteps([...oldSteps, { action }]);
    const response = await sendPerformAction(action, session_token);
    setSteps([...oldSteps, { action, result: response }]);
  }

  if (!overview || paused) {
    return <Menu onStartGame={startGame} onResumeGame={resumeGame} canResumeGame={paused} />
  } else {
    const onPerformAction = (action: string) => performAction(action, overview.session_token);
    return <Main overview={overview} steps={steps} onPerformAction={onPerformAction} onPause={pauseGame} />
  }
}
