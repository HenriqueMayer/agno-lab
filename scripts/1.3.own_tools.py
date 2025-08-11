from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools

from dotenv import load_dotenv

load_dotenv()


# Functions
def celsius_to_fhahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


agent = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[
        TavilyTools(),
        celsius_to_fhahrenheit,
    ],
)

agent.print_response(
    "Use your tools to search for the Porto Alegre, Brazil weather forecast for today. The result must be in Celsius."
)
