import pandas as pd
from scipy.constants import carat

df= pd.read_csv("../Day_05_07_07_2025/diamonds.csv")
#print(df)

"""below two lines is to get all the columns names of the df"""
# column_names=df.columns
# print(column_names)
#
# """below two lines is to get the data types of the df"""
# df_data_types=df.dtypes
# print(df_data_types)

#
# """below two lines is to drop a column from the  df """
# df.drop("Unnamed: 0", axis = 1 , inplace=True)
# print(df.columns)


# """below line is to read only carat column"""
# specific_column=df['carat']
# print(specific_column)

"""below line is to read more than one columns"""
# specific_column=df['carat',"cut"]
# print(specific_column)


"""below is to fetch only the row from 0 to 199 from all the columns"""
# data = df[0:200]
# print(data)

"For capturing more than 2 columns use the loc function"
# data = df.loc[0:200,["carat","cut"]]
# print(data)

"Gives the unique values present under the cut column"
# category_details = df["cut"].unique()
# print(category_details)

"""Gives the under cut columns how many different values are present + how many time each value present"""
# category_details = df["cut"].value_counts()
# print(category_details)


"""Give in numbers how many unique values"""
# category_details = df["cut"].nunique()
# print(category_details)

"""Gives the column name and there non-null count, and data type"""
# df_information = df.info()
# print(df_information)


"""Gives the mathematical column details like count, mean, std, min 25%, 50%, 75%, max """
df_description = df.describe()
print(df_description)