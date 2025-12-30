import { API_URL } from "./config";

export interface StartGameResponse {
    session_token: string;
    setting: string;
    beginning: string;
    goal: string;
}


export async function sendStartGame(): Promise<StartGameResponse> {
    const response = await fetch(`${API_URL}/start-game`, {
        method: "POST",
    });
    const body = await response.json();
    return body;
}
