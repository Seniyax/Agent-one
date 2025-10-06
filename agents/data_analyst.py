from crewai import Agent
from services.summarizer_tool import summarize_expenses_tool

def create_data_analyst_agent():
    return Agent(
        role="data_analyst",
        goal="Analyze the user's spending habits using their expense data.",
        backstory="An expert in personal finance who uses data tools to summerize and detect patterns.",
        llm="gpt-4o-mini",
        verbose=True,
        tools=[summarize_expenses_tool]
    )