# import necessary python libraries
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools
from agno.os import AgentOS

# create the AI investment agent
agent = Agent(
    name="PSX Investment Agent",
    model=Gemini(id="gemini-2.5-flash"),
    tools=[YFinanceTools()],
    description="You are an investment analyst specialising in the Pakistan Stock Exchange (PSX) who also covers global markets. You research stock prices, analyst recommendations, and stock fundamentals. For Pakistani companies, use the PSX ticker with the .KA suffix on Yahoo Finance (e.g., OGDC.KA, LUCK.KA, ENGRO.KA, HBL.KA, SYS.KA, MCB.KA).",
    instructions=[
        "Format your response using markdown and use tables to display data where possible.",
        "When comparing stocks, provide detailed analysis including price trends, fundamentals, and analyst recommendations.",
        "Always provide actionable insights for investors."
    ],
    debug_mode=True,
    markdown=True,
)

# UI for investment agent using AgentOS
agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="investment_agent:app", reload=True)
