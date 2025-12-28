import { sendPerformAction } from "@/libs/sendPerformAction";
import { sendStartGame } from "@/libs/sendStartGame";
import "@testing-library/jest-dom";
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import Game from "./Game";

jest.mock("@/libs/sendStartGame");
jest.mock("@/libs/sendPerformAction");

describe("Game Component Integration", () => {
    beforeEach(() => {
        jest.clearAllMocks();
    });

    it("plays through a full game loop", async () => {
        const mockOverview = {
            session_token: "session-123",
            setting: "Fantasy World",
            beginning: "You are in a dark room.",
            goal: "Escape.",
        };

        const mockActionResult = {
            outcome: "You open the door and see light.",
            quests: ["Escape"],
            inventory: ["Key"],
            world: "Corridor",
        };

        (sendStartGame as jest.Mock).mockResolvedValue(mockOverview);
        (sendPerformAction as jest.Mock).mockResolvedValue(mockActionResult);

        render(<Game />);

        // Start the game
        const startButton = screen.getByText(/start/i);
        fireEvent.click(startButton);
        expect(sendStartGame).toHaveBeenCalledTimes(1);

        // Verify Main component is rendered with overview
        await waitFor(() => {
            expect(screen.getByText(mockOverview.beginning)).toBeInTheDocument();
        });

        // Perform an action
        const input = screen.getByPlaceholderText("Describe an action of your character...");
        const enterButton = screen.getByText("Enter");
        fireEvent.change(input, { target: { value: "Open door" } });
        fireEvent.click(enterButton);

        // Verify sendPerformAction was called with correct args
        expect(sendPerformAction).toHaveBeenCalledWith("Open door", "session-123");

        // Verify the action and result are displayed
        await waitFor(() => {
            expect(screen.getByText(`> Open door`)).toBeInTheDocument();
            expect(screen.getByText(mockActionResult.outcome)).toBeInTheDocument();
        });

        // Pause the game
        const escButton = screen.getByText("Esc");
        fireEvent.click(escButton);

        // Verify Menu is shown again with Resume option
        await waitFor(() => {
            expect(screen.getByText(/resume/i)).toBeInTheDocument();
        });

        // Resume the game
        const resumeButton = screen.getByText(/resume/i);
        fireEvent.click(resumeButton);

        // Verify we are back to the game state
        await waitFor(() => {
            expect(screen.getByText(mockOverview.beginning)).toBeInTheDocument();
            expect(screen.getByText(mockActionResult.outcome)).toBeInTheDocument();
        });
    });
});