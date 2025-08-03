#Shahul Hameed



import matplotlib.pyplot as plt
import pandas as pd
from numpy.testing.print_coercion_tables import print_new_cast_table
from sklearn.preprocessing import  OneHotEncoder
import matplotlib.pyplot as plt


df = pd.read_csv("airlines_flights_data.csv")
print(df)


#Finding the null values in all columns
finding_null = df.isnull().sum().sum()
print("Printing the Null",finding_null)
# Outpyt= 0  Since there was not null did not use any method to fill like simple inputting

#Finding the Duplicates
find_dupli = df[df.duplicated()]
print("Duplicates are ---->",find_dupli)
# Output --->Duplicates are ----> Empty DataFrame



# Using the oneHot Encoder
one_hot_encoder = OneHotEncoder(sparse_output=False)
encoder_data = one_hot_encoder.fit_transform(df[["airline"]])

print(encoder_data)


encoded_df  = pd.DataFrame(encoder_data, columns=one_hot_encoder.get_feature_names_out())
print(encoded_df)


# Plotting the Graph
x= df["airline"]
y= df["duration"]

price= df["price"]
dur= df["duration"]

plt.scatter(x, y, color="red")
# plt.show()

# not working
# plt.bar(x,y)
# plt.show()


flight_counts = df["airline"].value_counts()
plt.pie(flight_counts, labels=flight_counts.index, autopct='%1.1f%%')
# plt.show()
