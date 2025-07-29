import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

"""Converting categorical to numerical data using the label encoder"""
df =  pd.read_csv("diamonds.csv")
print(df)
label_encoder_obj = LabelEncoder()
df['cut'] = label_encoder_obj.fit_transform(df['cut'])
print(df)
print(df.dtypes)


"""Shows Mapping of category to number done by Label encoder"""
label_mapping = dict(zip(label_encoder_obj.classes_,label_encoder_obj.fit_transform(label_encoder_obj.classes_)))
print(label_mapping)



