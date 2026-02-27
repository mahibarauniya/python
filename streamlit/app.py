import streamlit as st

st.title("Hello, Streamlit! 👋")
st.write("Welcome to your first Streamlit app.")

############# to take input from user and display it back #############
# name = st.text_input("What's your name?")
# if name:
#     st.success(f"Hello, {name}! 🎉")


############# Other Streamlit Important functions #############
# st.title("🎯 Main Title")
# st.header("📌 Header")
# st.subheader("🔹 Subheader")
# st.text("Plain text output")
# st.markdown("**Bold**, *Italic*, `code`, [link](https://streamlit.io)")
# st.caption("Small caption text")
# st.code("print('Hello, Streamlit!')", language="python")
# st.latex(r"E = mc^2")

# # Divider
# st.divider()

# # Write (smart display — works with almost anything)
# st.write("This is a string")
# st.write(42)
# st.write({"key": "value"})

## display pandas dataframe

############# PANDAS #############

# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 35],
#     "Score": [88.5, 92.3, 78.0]
# })

# # Display a table
# st.dataframe(df)                     # Interactive table
# st.table(df)                          # Static table
# st.data_editor(df)                    # Editable table

# # Display metrics
# col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "23°C", "+1.2°C")
# col2.metric("Accuracy", "94.2%", "-0.5%")
# col3.metric("Users", "1,250", "+50")

# # Display JSON
# st.json({"name": "Alice", "age": 25, "active": True})


import streamlit as st

# Text input
name = st.text_input("Enter your name", placeholder="e.g. Alice")
st.write(f"Hello, {name}!")

# Number input
age = st.number_input("Your age", min_value=1, max_value=120, value=25)

# Slider
rating = st.slider("Rate this app", 0, 10, 5)

# Select box
language = st.selectbox("Favorite language", ["Python", "JavaScript", "Go", "Rust"])

st.write(f"Language: {language}")
# Multiselect
skills = st.multiselect("Your skills", ["ML", "Data Viz", "NLP", "CV", "MLOps"])

# Radio buttons
level = st.radio("Experience level", ["Beginner", "Intermediate", "Expert"])

# Checkbox
agree = st.checkbox("I agree to the terms")
if agree:
    st.success("Thanks for agreeing!")

# Toggle
dark_mode = st.toggle("Enable Dark Mode")

# Date & Time
dob = st.date_input("Date of birth")
time = st.time_input("Meeting time")

# Color picker
color = st.color_picker("Pick a color", "#FF4B4B")

# Button
if st.button("🚀 Submit"):
    st.balloons()
    st.success("Submitted successfully!")