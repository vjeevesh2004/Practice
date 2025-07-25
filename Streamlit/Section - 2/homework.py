import streamlit as st
from datetime import datetime

st.title("Age Calculator")
st.subheader("Calcaulte your age from entered DOB")
dob = st.date_input("Select your date of birth: ")

st.write(f"Your DOB is: {dob}") 
today = datetime.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
st.write(f"Your age is: {age} years")       
st.write("Your age has been calculated successfully!")    
