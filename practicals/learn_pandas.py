# features
# series,dataframe,read csv,read json,viewing the data,data cleaning,plotting

# series
# it is like a column in a table,one-dimensional
import pandas as pd
# 1
a=[1,7,2]
var=pd.Series(a)
print(var)

# 2.creating label
a=[1,7,2]
var2=pd.Series(a,index=['x','y','z'])
print(var2)

# 3.key/value object
data={'day1':420,'day2':332,'day3':789}
var3=pd.Series(data)
print(var3)

# Data Frames
data2={
    'calories':[420,783,90],
    'time':[60,90,30]
}
var4=pd.DataFrame(data2)
print(var4)

# read csv
import pandas as pd
#to max rows
pd.options.display.max_rows=10
pd.options.display.max_columns=10
df1=pd.read_csv("data1.csv")
print(df1)

# read json
df2=pd.read_json("jsonfile_1.json")
print(df2.to_string())

# viewing data
import pandas as pd
df3=pd.read_csv("data1.csv")
print(df3.info())