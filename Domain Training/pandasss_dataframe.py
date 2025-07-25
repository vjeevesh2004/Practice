'''
dataframe is a 2d labeled data structure with rows and columns. 

it is mutable
heterogenous data type

three components - data, row, columns
'''
import pandas as pd
dataa = {
    "calories": [420, 380, 390],
    "duration": [50,40,45]    
}

df = pd.DataFrame(dataa)
print(df)
print(df.loc[[0,1]])
print(df.loc[[0,2]])
df = pd.DataFrame(dataa, index = ["day1", "day2", "day3"])
print(df)
print(df.loc["day2"])
df = pd.read_csv('data.csv')
print(df)