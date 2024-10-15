import streamlit as st
import pandas as pd
import Data_Analysis.numpy as np

# Title of the app
st.title("Hello Streamlit")

# Write a DataFrame
st.write("This is a simple text")

# Write a DataFrame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

# Display the DataFrame
st.write(df)

# Create a linechart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
