import streamlit as st

st.title("Hello, Chai app") # broad title 
st.subheader("Brewed with streamlit") # below title, will print this
st.text("Welcome to your first interactive app") # will print th e
st.write("Choose your fav. variety of chai")

# this will bring dropdown menu
chai = st.selectbox("Your Fav chai: ", ["Masala chai", "Lemon Tea", "Adarak Chai", "Kesar Chai"])

st.write(f"Your choose: {chai}. Excellent choice!")

st.success("Your chai has been brewed success")