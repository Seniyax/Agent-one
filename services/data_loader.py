import pandas as pd

def load_expenses(file_path):
    """Load expenses from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return None
    

def summerize_expenses(df: pd.DataFrame):

    """Summarize expenses by category."""
    
    summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    total = df
    return summary, total
   