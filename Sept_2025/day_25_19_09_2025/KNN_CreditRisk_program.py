import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np

# 1. Create a synthetic dataset for demonstration

data = {
    'income': [50000, 75000, 30000, 100000, 45000, 80000, 35000, 60000, 120000, 25000],
    'loan_amount': [15000, 20000, 5000, 50000, 10000, 25000, 8000, 18000, 70000, 4000],
    'credit_history_length': [5, 10, 2, 15, 4, 11, 3, 7, 20, 1],
    'risk': [0, 0, 1, 0, 0, 0, 1, 0, 0, 1]  # 0 = Low Risk, 1 = High Risk
}
df = pd.DataFrame(data)

# Define features (X) and target (y)
X = df[['income', 'loan_amount', 'credit_history_length']]
y = df['risk']

# 2. Split the data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Scale the feature data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Initialize and train the KNN classifier

k = int(np.sqrt(len(X_train)))
# Ensure k is an odd number to avoid ties in classification
if k % 2 == 0:
    k += 1

knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)

# 5. Make predictions and evaluate the model
y_pred = knn.predict(X_test_scaled)

print("Predictions:", y_pred)
print("Actual values:", np.array(y_test))
print("\nAccuracy Score:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 6. Predict the risk of a new, unseen applicant
# Create a new applicant's data
new_applicant = pd.DataFrame({
    'income': [32000],
    'loan_amount': [9000],
    'credit_history_length': [3]
})

# Scale the new applicant's data using the *same scaler* trained on the training data
new_applicant_scaled = scaler.transform(new_applicant)

# Predict the risk class
prediction = knn.predict(new_applicant_scaled)
predicted_risk = "High Risk" if prediction[0] == 1 else "Low Risk"

print("\n--- New Applicant Prediction ---")
print(f"The new applicant is classified as: {predicted_risk}")





























