# to work with data files and all

import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

file = st.file_uploader("Upload your csv file", type = ["csv"])

if file:
   df =  pd.read_csv(file)
   st.subheader("Data Preview")
   st.dataframe(df)

# after all this the file will be uploaded and 
# the preview of the data will be there
# there we cna sort the data, download the data and many other optiosj

if file:
   st.subheader("Summary Stats")
   st.write(df.describe())

# after this uplaod file again and summary of data showm

if file:
   cities = df["City"].unique()
   selected_city = st.selectbox("Filter By Cities", cities)
   filtered_data = df[df["City"] == selected_city ]
   st.dataframe(filtered_data)

# this will filter the data based on city

