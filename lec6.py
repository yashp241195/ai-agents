import json
from phi.agent.duckdb import DuckDbAgent
from phi.model.groq import Groq

DuckDbAIAgent_analyst = DuckDbAgent(
    model=Groq(id="llama3-70b-8192"),  
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Contains information about movies from IMDB.",
                    "path": "https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
                }
            ]
        }
    ),
    markdown=True,
)

DuckDbAIAgent_analyst.print_response(
    "What is the total count of all movies? "
    "What is the total sum of the ratings of all movies? "
    "What is the average rating of all movies? ",
    stream=True,
)
