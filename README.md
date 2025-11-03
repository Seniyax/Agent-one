
https://github.com/user-attachments/assets/a04ef170-89ac-4b0f-ba50-54408766e733
# Personal Finance Tracker Agent
An **AI-powered multi-agent system** that helps users **analyze personal expenses**, **track spending habits**, and **generate financial summaries and reports** automatically.  
Built with **CrewAI**, **OpenAI API**, and **Streamlit**, this project demonstrates how multiple autonomous agents can collaborate to process data, derive insights, and generate natural language outputs.

## Features
- **Multi-Agent Colloboration:** Three CrewAI agents (Data Analyst, Report generator & summarizer tool) work together.
- **Expense Summarization:** Reads and summarizes spending data from CSV files.
- **Automated Report Generation:** Produces natural language financial summaries.

## Architecture Overview
  <img width="1000" height="1123" alt="diagram-export-10-8-2025-12_15_27-PM" src="https://github.com/user-attachments/assets/a63ffd2d-94c8-4b54-b65f-889ad5469f6c" />

## Project Structure
````bash
Agent-one/
│
├── agents/
│      ├── data_analyst.py
│      ├── finance_advisor.py
│      └── report_generator.py
├──  services/
│         ├── data_loader.py
│         ├── report_tool.py
│         └── summarizer_tool.py
├── app.py
├── crew.py
├── test.py
└── README
````

## How it works ?
1. The user uploads an expense CSV file via the Streamlit UI.
2. The Finance Analyst Agent reads the file and uses a tool to calculate total and category spending.
3. The Report Generator Agent takes that output and produces a natural language report summarizing financial insights.
4. The Streamlit UI displays both the structured summary and report interactively.

## Tech stack
- Python
- CrewAI
- OpenAI API
- Pandas
- Streamlit

## Installation and Setup
- Clone the repository
  ````bash
  git clone https://github.com/seniyax/Agent_one.git
  cd personal-finance-agent
  ````
- Run the streamlit ui
  ````bash
  streamlit run ui/app.py
  ````
  
## Future Enhancements
- Monthly trend analysis with charts.
- Budget recommendation agent.
- Multi-currency and localization support



https://github.com/user-attachments/assets/91f9527b-4580-4a63-87c8-f7acf754e94d

