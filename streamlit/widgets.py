import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name")

age = st.slider("Enter your age", 0, 130)

st.write(f"Your age is {age}")

options = ["Python", "Java", "C++", "Ruby", "JavaScript"]
choice = st.selectbox("Choose a programming language", options)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello {name}")

data = {
    "name": ["John", "Anna", "Peter", "Linda"],
    "age": [23, 45, 32, 54],
    "programming language": ["Python", "Java", "C++", "Ruby"]
}
df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)