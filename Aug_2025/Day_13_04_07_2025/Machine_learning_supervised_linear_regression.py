import pandas as pd
from sklearn.linear_model import  LinearRegression
from utilities.file_reading import data_to_data_frame

"""Below input contains year and house price for the dataframe"""
my_input = {
    "year":[2000,2001,2002,2003,2004,2005,2006,2007],
    "house_price" :[8000,9000,10000,11000,12000,13000,14000,15000]
}


"""Below is the user defined function for converting data into dataframe"""

# def data_to_data_frame(data): #Function definition with argument
#     """Below code is with exception handling for dataframe conversion"""
#     try:
#         df = pd.DataFrame(data)
#         print(df)
#         print(type(df))
#     except Exception as ex:
#         print(ex)
#
#
# data_to_data_frame(my_input)


"""Using the return method same function"""

# def data_to_data_frame(data): #Function definition with argument
#     """Below code is with exception handling for dataframe conversion"""
#     try:
#         df = pd.DataFrame(data)
#         return  df
#     except Exception as ex:
#         print(ex)
#
#
# returned_Data = data_to_data_frame(my_input) #function calling
# print(returned_Data)


""" Keep the above function as utility"""

# df = data_to_data_frame(my_input) #function calling
# print(df)
#
# x = df[["year"]]  #Independent variable will be in double bracket
# y = df["house_price"]  #Dependent variable wll be in single bracket
#
# model = LinearRegression()
# model.fit(x, y) #training
#
#
# #Below we are giving the new value to predict the output , However till model.fit we are training the data
# my_input = {"year":[2009,2010]}
# input_df = data_to_data_frame(my_input)
#
# my_prediction = model.predict(input_df)
# print(my_prediction)


""" Now converting the above model as function """

# df = data_to_data_frame(my_input) #function calling
# print(df)
#
# x = df[["year"]]  #Independent variable will be in double bracket
# y = df["house_price"]  #Dependent variable wll be in single bracket
#
# """Converted has model now"""
# def model_training(model_name):
#     try:
#         model= model_name
#         model.fit(x, y) #training
#         return  model
#     except Exception as ex:
#         return  ex
#
# #Below we are giving the new value to predict the output , However till model.fit we are training the data
# my_input = {"year":[2009,2010]}
# input_df = data_to_data_frame(my_input)
#
# model = model_training(LinearRegression())
# my_prediction = model.predict(input_df)
# print(my_prediction)


""" Now converting the predication lines of code as re-usable function, will take the above program"""

df = data_to_data_frame(my_input) #function calling
print(df)

x = df[["year"]]  #Independent variable will be in double bracket
y = df["house_price"]  #Dependent variable wll be in single bracket

z=10

"""Converted has model now"""
def model_training(model_name):
    try:
        model= model_name
        model.fit(x, y) #training
        return  model
    except Exception as ex:
        return  ex

