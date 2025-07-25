import streamlit as st

st.title("Chai Maker app")

if st.button("Make Chai"):
    st.success("Your Chai is being brewed") 

# nothing will happen if didn't add this checkbox in variable

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your Chai")

tea_type = st.radio("Pick your chai base ", ["Milk", "Water", "Sugar"])
st.write(f"Selected Base {tea_type}")

flavour = st.selectbox("Choose flavour: ", ["Adrak", "Tulsi", "Kesar"])
st.write(f"Selected flavour: {flavour}")

sugar_level = st.slider("Sugar level: ", 0, 5, 2) # here 2 is the default value
st.write(f"Sugar level selected: {sugar_level}. Successfully!")

cup = st.number_input("How many cups", min_value = 1, max_value = 10, step = 1)
st.write(f"Selected sugar level: {cup}")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Welcome {name}! , your Chai is on the way")

# search all types of input can be taken

dob = st.date_input("Select your date of birth: ")
st.write(f"Your DOB is: {dob}")

# prepare a age calculator