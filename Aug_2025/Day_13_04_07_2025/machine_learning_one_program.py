import pandas as pd
from sklearn.linear_model import  LinearRegression
from utilities.file_reading import data_to_data_frame

"""Below input contains year and house price for the dataframe"""
my_input = {
    "year":[2000,2001,2002,2003,2004,2005,2006,2007],
    "house_price" :[8000,9000,10000,11000,12000,13000,14000,15000]
}

df = data_to_data_frame(my_input) #function calling
print(df)

x = df[["year"]]  #Independent variable will be in double bracket
y = df["house_price"]  #Dependent variable wll be in single bracket

model =  LinearRegression()
model.fit(x,y)

input_df = {"year":[2009,2010]}
input_df = pd.DataFrame(input_df)
my_prediction = model.predict(input_df)
print(my_prediction)
