# Personal Finance Tracker Agent
An **AI-powered multi-agent system** that helps users **analyze personal expenses**, **track spending habits**, and **generate financial summaries and reports** automatically.  
Built with **CrewAI**, **OpenAI API**, and **Streamlit**, this project demonstrates how multiple autonomous agents can collaborate to process data, derive insights, and generate natural language outputs.

## Features
- **Multi-Agent Colloboration:** Three CrewAI agents (Finance Analyst & Report Generator) work together.
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
├──  tools/
│         ├──
│         └── 
