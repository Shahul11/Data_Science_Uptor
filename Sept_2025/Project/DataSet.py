import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import matplotlib.pyplot as plt


# Simulated customer data

"""

# My Understanding
- Seed: Ensures reproducibility of random numbers.  Every time  I run i get different data's which is taken care by seed, we can give any number other than 42 too also
- n_samples: Number of  customers i.e 200

"""


np.random.seed(42)
n_samples = 200

data = pd.DataFrame({
    'income': np.random.normal(60000, 15000, n_samples).astype(int),
    'loan_amount': np.random.normal(20000, 8000, n_samples).astype(int),
    'credit_history': np.random.randint(1, 20, n_samples),
    'age': np.random.randint(20, 60, n_samples),
    'risk': np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3])  # 0 = Low Risk, 1 = High Risk
})


"""
used - StandardScaler:  To Normalizes data  so that we dont have exterme values of loan amount or income .

"""



# Features for clustering
X_cluster = data[['income', 'loan_amount', 'credit_history', 'age']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_cluster)

""" 
Using the scaled data and with cluster size of 4 

Scales features to mean 0 and variance 1  as it is important to apply  for distance-based algorithms like K-Means.


- Creates 4 clusters.
- Assigns each customer to a cluster (0, 1,2 ,3), stored in a new column.


"""


# K-Means
kmeans = KMeans(n_clusters=4, random_state=42)
data['cluster'] = kmeans.fit_predict(X_scaled)



""" Now applying the KNN algorithm for the same
 
 
 - X_knn: Features including the cluster label.
- y_knn: Target variable (risk).

 
 """

# Features for KNN (including cluster)
X_knn = data[['income', 'loan_amount', 'credit_history', 'age', 'cluster']]
y_knn = data['risk']

# Train-test split   - Splits data into 70% training and 30% testing.
X_train, X_test, y_train, y_test = train_test_split(X_knn, y_knn, test_size=0.3, random_state=42)

# Standardize  Scaling the data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# KNN model


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Predict and evaluate
y_pred = knn.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

plt.scatter(X_scaled[:, 0], X_scaled[:, 1], cmap='viridis')
plt.title("Customer Segments via K-Means")
plt.xlabel("Income (scaled)")
plt.ylabel("Loan Amount (scaled)")
plt.show()
