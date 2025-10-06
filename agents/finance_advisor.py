from crewai import Agent,Task


def create_finance_advisor():
    return Agent(
        role="Financial Advisor",
        goal="Give the user budgeting and savingd recommendations based on their spending.",
        backstory="A professional financial advisor focused on personal budgeting and cost optimizations.",
        llm="gpt-4o-mini",
        verbose=True
    )