from phi.model.groq import Groq
from textwrap import dedent
from datetime import datetime

from phi.agent import Agent
from phi.tools.exa import ExaTools

# Fixing missing or wrong import, `ExaTools` might need adjustment if not available
# Assuming `ExaTools` is the correct tool for keyword search

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),  # Assuming Groq model loading is correct
    tools=[ExaTools(start_published_date=datetime.now().strftime("%Y-%m-%d"), type="keyword")],  # Check if ExaTools has the right parameters
    description="You are an advanced AI researcher writing a report on a topic.",
    instructions=[
        "For the provided topic, run 3 different searches.",
        "Read the results carefully and prepare a NYT worthy report.",
        "Focus on facts and make sure to provide references.",
    ],
    expected_output=dedent("""\
    An engaging, informative, and well-structured report in markdown format:

    ## Engaging Report Title

    ### Overview
    {give a brief introduction of the report and why the user should read this report}
    {make this section engaging and create a hook for the reader}

    ### Section 1
    {break the report into sections}
    {provide details/facts/processes in this section}

    ... more sections as necessary...

    ### Takeaways
    {provide key takeaways from the article}

    ### References
    - [Reference 1](link)
    - [Reference 2](link)
    - [Reference 3](link)

    - published on {date} in dd/mm/yyyy
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,  # You want to add datetime dynamically to instructions
    save_response_to_file="tmp/{message}.md",  # Saving response to a markdown file
)

# Assuming 'Simulation theory' is a valid search topic and Agent has a `print_response` method
agent.print_response("Simulation theory", stream=True)
