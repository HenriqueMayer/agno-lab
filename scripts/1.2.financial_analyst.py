from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools

from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[YFinanceTools(), TavilyTools()],
    instructions="Use tables to present the data. Don't insert any other text.",
)

agent.print_response("Use your tools to search for the ADP stock prices", stream=True)
