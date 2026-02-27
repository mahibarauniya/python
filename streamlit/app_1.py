import streamlit as st
from main_1 import run, add_numbers, process_data

st.title("My Streamlit App")

# Call a function from main.py
result = run()
st.write(result)

# Use another function
answer = add_numbers(5, 10)
st.success(f"Result: {answer}")