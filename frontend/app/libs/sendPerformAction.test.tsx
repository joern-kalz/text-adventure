import { sendPerformAction } from "./sendPerformAction";

global.fetch = jest.fn();

describe("sendPerformAction", () => {
    beforeEach(() => {
        jest.clearAllMocks();
    });

    it("sends a POST request with the correct headers and body", async () => {
        const mockResponseData = {
            outcome: "You move north.",
            quests: ["Explore"],
            inventory: ["Map"],
            world: "Forest",
        };

        (global.fetch as jest.Mock).mockResolvedValue({
            json: jest.fn().mockResolvedValue(mockResponseData),
        });

        const action = "move north";
        const sessionToken = "abc-123";

        const result = await sendPerformAction(action, sessionToken);

        expect(global.fetch).toHaveBeenCalledTimes(1);
        expect(global.fetch).toHaveBeenCalledWith("http://localhost:8000/perform-action", {
            method: "POST",
            body: JSON.stringify({ action }),
            headers: {
                "x-session-token": sessionToken,
                "Content-Type": "application/json",
            },
        });

        expect(result).toEqual(mockResponseData);
    });
});