import pandas as pd
from sklearn.preprocessing import  OneHotEncoder

df = pd.read_csv("diamonds.csv")

one_hot_encoder = OneHotEncoder(sparse_output=False)
encoder_data = one_hot_encoder.fit_transform(df[['cut']])
print(encoder_data)