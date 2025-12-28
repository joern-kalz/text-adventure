export interface StartGameResponse {
    session_token: string;
    setting: string;
    beginning: string;
    goal: string;
}

export async function sendStartGame(): Promise<StartGameResponse> {
    const response = await fetch("http://localhost:8000/start-game", {
        method: "POST",
    });
    const body = await response.json();
    return body;
}
