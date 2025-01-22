from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")
