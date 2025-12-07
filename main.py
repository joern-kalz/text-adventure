import getpass
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field


class Overview(BaseModel):
    """Overview of the game"""

    setting: str = Field(
        description="Description of an imaginative game setting in a few words like ancient Greece"
    )
    beginning: str = Field(
        description="Description of the location where the player starts in 2-3 sentences"
    )
    goal: str = Field(
        description="Description of the goal the player must reach to succeed in the game"
    )


load_dotenv()
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
structured_llm = model.with_structured_output(Overview)

overview_response = structured_llm.invoke(
    "Describe the setting, beginning, and goal for a random role-playing game."
)

print("Game overview Response:", overview_response)

agent = create_agent(
    model="google_genai:gemini-2.5-flash",
    system_prompt=f"""
    ## ROLE

    You are the gamemaster for an immersive role-playing game. 

    ## RULES OF INTERACTION
    
    In each turn the player will describe an action their character wants to take. You will describe the outcome of that action.

    If the player writes anything that is not an action of their character, you will ask them to rephrase it as an action of their character.

    The outcome you describe must be logical and consistent with the current state of the game world. If the action is impossible, you must describe the negative outcome. 

    Focus on sight, sound, smell, and texture in your descriptions. 
    
    Never describe the Player's actions, emotions or speech for them. Only describe the outcome of their actions.

    Always use the second person ("you") when addressing the player.

    ## RESPONSE FORMAT

    Always respond in the following JSON format:
    {{
        "outcome": "<description of the outcome of the action in 3-5 sentences>",
        "quests": [<list of current quests the player is undertaking>],
        "inventory": ["<list of all items the player is carrying>"],
        "world": "<detailed description of the current state of the whole game world>",
    }}

    ## Game Setting
    
    {overview_response.setting}

    ## Game Beginning
    
    {overview_response.beginning}

    ## Game Goal
    
    {overview_response.goal}
    """,
    checkpointer=InMemorySaver(),
)

while True:
    r = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": input("Enter an action of your character: "),
                }
            ]
        },
        {"configurable": {"thread_id": "1"}},
    )

    print(r["messages"][-1].content)
