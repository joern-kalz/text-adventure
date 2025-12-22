"""Generates the prompt for the game overview agent."""


def get_game_overview_prompt() -> str:
    """Generates the system prompt text for the gamemaster agent."""

    return """
        ## TASK

        Generate an overview of a text adventure game including:

        1. An imaginative game setting in a few words. Create something similar, but not identical to the following examples: 'Ancient Athene during the reforms of Solon', 'Mediaeval fantasy world with elves, trolls, and a dragon', 'Fairy tale world with a giant, a fairy godmother, and a wolf', 'Cyberpunk city on Mars after the fall of the empire'
        2. A description of the location where the player starts in 2-3 sentences
        3. A precise description of a single goal the player must reach to succeed in the game.
        
        Never describe the Player's actions, emotions or speech for them.

        Always use the second person ("you") when addressing the player.

        ## RESPONSE FORMAT

        You must adhere to the following strict rules:

        1. Output **only** valid JSON.
        2. Do not offer any explanations, headers, or conversational filler.
        3. Do not use Markdown code blocks (e.g., do not start with ```json).
        4. Follow this exact JSON schema:

        {
            "setting": "Imaginative game setting.",
            "beginning": "Location where the player starts",
            "goal": "Goal the player must reach."
        }
        """
