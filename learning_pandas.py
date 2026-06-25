# When working with tabular data, such as data stored in spreadsheets or databases, pandas is the right tool
# Importing data from each of these data sources is provided by function with the prefix read_*.
# Similarly, the to_* methods are used to store data.
# In pandas the data table is called a Dataframe-->2-dimentional,Series-->1-dimentional
# using matplotlib you can plot the data
# used to analyze data
# working with data sets
# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008

import pandas as pd

db=pd.read_csv("C:/Users/prnir/PycharmProjects/NGO_Data of State- UTTAR PRADESH, from 1 to 3770.csv")

db.head(5)

mydata={
    'cars':['BMW','BENZ','AUDI'],
    'price':[220,300,203]
}
print(pd.DataFrame(mydata))


# series:#one dimentional(like a column in a table)

import pandas as pd
a=[10,12,30]
print(pd.Series(a))

#If nothing else is specified, the values are labeled with their index number.
# First value has index 0, second value has index 1 etc.

import pandas as pd
a=[1,5,3]
the_var=pd.Series(a)
the_var[0]


import pandas as pd
a=[1,2,3]
the_var=pd.Series(a,index=['x','y','z'])
print(the_var)
the_var[0]

import pandas as pd
calories={'day1':'410','day2':'380','day3':323}
myvar=pd.Series(calories)
print(myvar)

calories={'day1':'410','day2':'380','day3':323}
myvar=pd.Series(calories,index=['day2','five'])#it will return not a number NaN because the index is not correct
myvar=pd.Series(calories,index=['day2','day3'])
print(myvar)

#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
import pandas as pd
mydata={
    'cars':['BMW','BENZ','AUDI'],
    'price':[220,300,203]
}

new_var=pd.DataFrame(mydata,index=['data1','data2','data3'])
print(new_var.loc['data1'])
print(new_var.loc[['data1','data2']])


# Load a comma separated file (CSV file) into a DataFrame
import pandas as pd
df=pd.read_csv("data1.csv",)
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows
print(df.to_string())#df.to_string to print the entire dataframe

