def run():
    print("Main logic running!")
    return "Hello from main.py"

def add_numbers(a, b):
    return a + b

def process_data(df):
    df["new_col"] = df["value"] * 2
    return df