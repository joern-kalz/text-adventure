
export interface PerformActionResponse {
    outcome: string
    quests: string[];
    inventory: string[];
    world: string;
}

export async function sendPerformAction(action: string, sessionId: string): Promise<PerformActionResponse> {
    const response = await fetch("http://localhost:8000/perform-action", {
        method: "POST",
        body: JSON.stringify({ action }),
        headers: {
            "x-session-id": sessionId,
        },
    });
    const body = await response.json();
    return body.message;
}
