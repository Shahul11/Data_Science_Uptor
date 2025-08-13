import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("house_price_bd.csv")
print(df)
column_names = df.columns
print(column_names)

# below is one way or else smartly drop the columns which you don't need that will be x value
# x = df[['Bedrooms', 'Bathrooms','Floor_no','Occupancy_status',
#        'Floor_area', 'City','Location']]

df.dropna(inplace=True)
df['Price_in_taka'] = df['Price_in_taka'].replace({"৳":"",",":""},regex=True).astype(float)

x = df.drop(['Price_in_taka','Title','City','Location','Floor_no','Occupancy_status'],axis=1)
y = df['Price_in_taka']



x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.7, random_state=42)

# random_state=42  # same shuffle order every time

model = LinearRegression()
model.fit(x_train,y_train)

y_predict = model.predict(x_test)
print(y_predict)


accuracy_check = r2_score(y_test,y_predict)
print(accuracy_check)