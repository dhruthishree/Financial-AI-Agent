from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

finance_agent = Agent(
    name="Finance Agent",
    description="An agent that can answer financial questions and provide stock information.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables for displaying the data"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

finance_agent.print_response("Summarize analyst recommendations for Apple Inc.", stream=True)
