import pandas as pd
from crewai.tools import tool

@tool
def summarize_expenses_tool(csv_path:str) -> str:
    """Read a CSV file of expenses from "data/sample_expenses.csv" and summarizes total and category spending"""
    csv_path = "data/sample_expenses.csv"

    df = pd.read_csv(csv_path)

    if not all(col in df.columns for col in ["Category","Amount"]):
        return "Invalid CSV format. Expect Amount and Category columns"
    
    total = df["Amount"].sum()
    by_category = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    top3 = by_category.head(3)

    summary = f"""
    Expense Summary :
    Total spent: ${total:.2f}
    Top 3 categories:
    {top3.to_string()}


    Full breakdown:
    {by_category.to_string()}
    """
    return summary



##summarize_expenses_tool = Tool(
    name = "Summerize Expenses",
    description="Read a CSV file of expenses and summarizes total and category spending.",
    func = summarize_expenses_tool
##)

