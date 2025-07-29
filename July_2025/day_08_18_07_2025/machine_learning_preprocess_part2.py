from enum import unique

import pandas as pd

df = pd.read_csv("diamonds.csv")
#print(df)

columns = df.columns
#print(columns)
#print(df.dtypes) #dtypes for more than one column

#To extract the object type from daimonds file


#mthod 1
# for col in columns:
#     if df[col].dtype == 'O':
#         print(col)


#method 2

# object_column = []
#
# for col in columns:
#     if df[col].dtype == 'O':
#         object_column.append(col)
# print(object_column)


# category_details =  df['carat'].value_counts()
# print("Catergorey detils:", category_details)

"""Convert categories into numerical values,  when you have less value go with this method below to convert from ojbect to  numerical"""
# cut_categories_list = df['cut'].unique()
# print(cut_categories_list)
#
# df.dropna(inplace=True)
# df.reset_index(inplace=True)
#
# df['cut'] = df['cut'].map({'Ideal':1, 'Premium':2, 'Good':3, 'Very Good':4 ,'Fair':8  })
# print(df)
# print(df.dtypes)


"""Conversion of categorical data into numerical data"""
from sklearn.preprocessing import  LabelEncoder
label_encoder_object = LabelEncoder()
df['cut'] = label_encoder_object.fit_transform(df['cut'])
print(df)
print(df.dtypes)
unique_data_post_conversion = df['cut'].unique()
print(unique_data_post_conversion)

"""Conversion of categorical data into numerical data for more than one column,
Note: Below code will through error you cannot convert 2 columns at one shot  or in one line you need to do it sperately"""
# from sklearn.preprocessing import  LabelEncoder
# label_encoder_object = LabelEncoder()
# df['cut','color'] = label_encoder_object.fit_transform(df['cut','color'])
# print(df)
# print(df.dtypes)
# unique_data_post_conversion = df['cut'].unique()
# print(unique_data_post_conversion)

""" Difference between Label and Ordinal Encoder, when you convert the categorical data ,

1. OrdinalEncoder returns encoded values as float64 by default; 
   LabelEncoder returns int64 values.

2. OrdinalEncoder shows NaN if a value is missing in the original column
    LabelEncoder does not show or preserve NaN — it drops or skips it silently

3. OrdinalEncoder supports multiple columns (2D data),
   while LabelEncoder only works on single-column (1D) targets.


"""



# from sklearn.preprocessing import  OrdinalEncoder
# ordinal_encoder_object = OrdinalEncoder()
# df['cut'] = ordinal_encoder_object.fit_transform(df[['cut','carat']])
# print(df)
# print(df.dtypes)
#
# unique_data_post_conversion = df['cut'].unique()
# print(unique_data_post_conversion)