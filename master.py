import streamlit as st
import pandas as pd
import numpy as np

st.title("Doing Streamlit") # title
st.header("Random Header")
st.write("Hello Learners!") # used to print content on screen

# Creates a dataframe
df = pd.DataFrame({
    'Name' : ['John', 'Bob', 'Mary', 'Adam'],
    'Marks' : [78, 56, 96, 82]
})

st.write("Description of the Data Frame")
st.write(df.describe())

st.write("Visualisation")
st.line_chart(df['Marks'])
