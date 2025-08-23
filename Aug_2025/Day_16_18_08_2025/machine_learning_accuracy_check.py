import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from  sklearn.preprocessing import  LabelEncoder





df = pd.read_csv("diamonds.csv")
print(df)

""" Converting the categorical column to Numbers"""

columns = df.columns
print(columns)

lbl = LabelEncoder()
df["cut"] = lbl.fit_transform(df["cut"])
df["color"] = lbl.fit_transform(df["color"])
df["clarity"] = lbl.fit_transform(df["clarity"])


df.drop("Unnamed: 0", axis=1, inplace=True)
print(df)


x = df.drop("price",axis=1)
y = df["price"]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, random_state=42)

model = LinearRegression()
model.fit(x_train,y_train)

y_predict = model.predict(x_test)
print(y_predict)


accuracy_check = r2_score(y_test,y_predict)
print(accuracy_check)








