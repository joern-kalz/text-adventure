import { sendStartGame } from "./sendStartGame";

global.fetch = jest.fn();

describe("sendStartGame", () => {
    beforeEach(() => {
        jest.clearAllMocks();
    });

    it("sends a POST request to start the game and returns the response", async () => {
        const mockResponseData = {
            session_token: "session-123",
            setting: "Fantasy World",
            beginning: "You are in a dark room.",
            goal: "Escape.",
        };

        (global.fetch as jest.Mock).mockResolvedValue({
            json: jest.fn().mockResolvedValue(mockResponseData),
        });

        const result = await sendStartGame();

        expect(global.fetch).toHaveBeenCalledTimes(1);
        expect(global.fetch).toHaveBeenCalledWith("http://localhost:8000/start-game", {
            method: "POST",
        });

        expect(result).toEqual(mockResponseData);
    });
});