import streamlit as st
import pandas as pd

st.title("Fetch and Display Data from a URL")

# Corrected URL with the right spelling of "population"
url = 'https://storage.dosm.gov.my/population/population_state.csv'

# Read the data from the URL
url_data = pd.read_csv(url)

st.subheader("Display Data from URL")
st.dataframe(url_data, use_container_width=True)
st.caption("Displaying data fetched from an online source")
