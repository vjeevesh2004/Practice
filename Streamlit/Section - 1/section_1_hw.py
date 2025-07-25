'''to build a similar app, built previously for chai, now for programming languages'''
import streamlit as st
st.title("Hello, Programming Language app")
# st.subheader("Made with streamlit")
st.write("Choose your favorite programming language")

prog_lang = st.selectbox("Your language: ", ["Python", "Java", "R", "C", "C++", "JavaScript","Scala", "Ruby"])

st.write(f"Your choosed: {prog_lang}. Great!")
st.success("You have choosed programming language successfully!")
st.text("Wish You All The Best")
st.text("Happy Coding!")