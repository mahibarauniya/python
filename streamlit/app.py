import streamlit as st
from main import add_numbers

st.title("Hello, Streamlit! 👋")
st.write("Welcome to your first Streamlit app.")

# Simple calculator using main.py
st.subheader("Simple Calculator")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

if st.button("Add"):
    result = add_numbers(num1, num2)
    st.write(f"Result: {num1} + {num2} = {result}")
