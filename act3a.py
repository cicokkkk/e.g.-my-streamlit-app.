import streamlit as st
import pandas as pd


st.title("Fetch and Display Data from Local Storage")


file_path = './restaurant.csv'
local_data = pd.read_csv(\Users\makmal.25-2634_moe-d\Desktop\dashboard)


st.subheader("Display Data from Local CSV File")
st.dataframe(local_data, use_container_width=True)
st.caption("Displaying data using st.dataframe")
