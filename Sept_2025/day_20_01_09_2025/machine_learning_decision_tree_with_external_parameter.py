import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import category_encoders as ce

column_names = ['buying_price', 'maintenance_cost', 'doors_numbers',
                'person_number', 'luggage_space', 'safety', 'class']
df = pd.read_csv("car_evaluation.csv", names=column_names, header=None)


label_encoder = LabelEncoder()
df['class'] = label_encoder.fit_transform(df['class'])

X = df.drop("class", axis=1)
y = df['class']

encoder = ce.OrdinalEncoder(cols=['buying_price', 'maintenance_cost', 'doors_numbers',
                                  'person_number', 'luggage_space', 'safety'])
X_encoded = encoder.fit_transform(X)
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_encoded, y)
y_pred = dt_model.predict(X_encoded)
print(y_pred)
