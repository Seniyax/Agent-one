from dotenv import load_dotenv
import os
from openai import OpenAI
from crewai import Crew,Process,Task
from agents.data_analyst import create_data_analyst_agent
from agents.finance_advisor import create_finance_advisor
from agents.report_generator import create_report_generator_agent

def run_process(file_path):

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    client = OpenAI(api_key=api_key)

    analyst = create_data_analyst_agent()
    advisor = create_finance_advisor()
    reporter = create_report_generator_agent()

    analyze_task = Task(
        description="Analyze the user's spending habits using their expense data.",
        agent=analyst,
        expected_output="A concise text summary of the user's spending patterns."
    )

    advise_task = Task(
        description="Provide budgeting and saving recommendations based on the spending analysis.",
        agent=advisor,
        expected_output="Personalized financial advice text with savings suggestions."
    )

    reporter_task = Task(
        description="Combine the expense summary and finanacial advice into a well-structured financial report.Format it neatly with sections and bullet points",
        agent=reporter,
        expected_output="A full financial report combining analysis and advice."

    )

    crew = Crew(
        agents=[analyst, advisor, reporter],
        tasks=[analyze_task, advise_task, reporter_task],
        process=Process.sequential,
        verbose=False
    )

    results = crew.kickoff()
   
    return results

