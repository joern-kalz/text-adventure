export interface StepResult {
    outcome: string
    quests: string[];
    inventory: string[];
    world: string;
}

export interface Step {
    action: string;
    result?: StepResult;
}

