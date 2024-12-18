import streamlit as st


st.title("My First Dashboard App")
         
st.write("Hello, welcome to my first Dashboard app!")

user_input = st.text_input("Enter your name:")



st.write(f"Congratultions, {user_input}! this is your first dashboard")