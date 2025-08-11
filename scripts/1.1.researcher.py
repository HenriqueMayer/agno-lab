from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools

from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.1-8b-instant"), tools=[TavilyTools()], debug_mode=True
)

agent.print_response(
    "Use your tools to search for the Porto Alegre/Brazil weather forecast for today."
)

# uv run 1.1.researcher.py
