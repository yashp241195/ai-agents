from phi.model.groq import Groq
from phi.agent import Agent
from phi.tools.exa import ExaTools

from dotenv import load_dotenv
load_dotenv()

# Creating the Author Research Agent
author_research_agent = Agent(
    name="Author Researcher",
    model=Groq(id="llama3-8b-8192"),  
    tools=[ExaTools()],
    markdown=True,
    description="You are an expert author research agent. Your role is to assist users in gathering detailed, customized information about authors, their works, awards, and literary influence.",
    instructions=[
        "Use Exa to search and extract relevant data from reputable literary platforms, databases, and websites.",
        "Collect information on the author's biography, notable works, literary awards, and cultural impact.",
        "Ensure that the gathered data is accurate and focused on the author's contributions, influences, and major literary achievements.",
        "Provide clear and concise summaries of the information, ensuring that it is easily understandable for the user.",
        "Last section must be dedicated to listing top sources of information used by Exa."
    ],
)

# Example query to gather author information
author_research_agent.print_response(
    "Find detailed information about the author Albert Camus, including his biography, notable works, literary influences, and awards.",
    stream=True,
)
