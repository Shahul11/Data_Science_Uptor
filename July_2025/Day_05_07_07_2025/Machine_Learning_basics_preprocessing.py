import pandas as pd
"""pip install pandas"""

"""this line will help is getting the output of entire rows"""
pd.set_option("display.max_rows",None)

"""below code is read the csv from current directory only"""
df = pd.read_csv("diamonds.csv")
# print(df)

"""below code is read the csv from other directories as well"""
# df = pd.read_csv(r"/Users/hp/Desktop/LMES/DS_ML/LMES_203_Monday_Friday/July_2025/Day_04_04_07_2025/diamonds.csv")
# print(df)

column_types = df.dtypes
print(column_types)

"""below code is to read first 10 rows only"""
# df = pd.read_csv("diamonds.csv")
# print(df.head(10))


"""below code is to read last 10 rows only"""
# df = pd.read_csv("diamonds.csv")
# print(df.tail(10))
