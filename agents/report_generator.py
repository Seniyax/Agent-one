from crewai import Agent
from services.report_tool import save_report_as_pdf

def create_report_generator_agent():
    return Agent(
        role="report_generator",
        goal="Combine analysis and advice into a structured financial report for the user.",
        backstory="An experienced financial report writer who presents data clearly and neatly.",
        llm= "gpt-4o-mini",
        tools= [save_report_as_pdf],
        verbose=False
     
    )
