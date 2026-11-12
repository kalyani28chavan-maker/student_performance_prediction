import streamlit as st
import pandas as pd 

st.title("student performance prediction")

data={
    "Name":["Anshika","Rahul","Priya","Amit"],
    "Study_Hours":[5,3,6,2],
    "Marks": [90,60,95,45]    
}

df = pd.DataFrame(data)

st.subheader("student  data")
st.dataframe(df) 