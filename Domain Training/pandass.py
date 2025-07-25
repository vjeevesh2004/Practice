'''
pandas is based on two data structures - series and dataframe
series - single dimensional array
dataframe - multiple dimensional array

each series is based on index value
user can give user define index value
'''

import pandas as pd
import numpy as np

daata = np.array(['Python','php','java'])
seriesss = pd.Series(daata)
print(seriesss)

# creating dataframes from list
daataaa = ['python', 'php', 'java']
s22 = pd.Series(daataaa, index = ['r1','r2', 'r3'])
print(s22)