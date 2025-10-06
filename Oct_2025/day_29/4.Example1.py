import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 🛍️ Sample customer data: [Orders/Month, Avg Cart Value]
X = np.array([
    [10, 3000],  # A
    [9, 2800],   # B
    [2, 500],    # C
    [3, 700],    # D
    [5, 1500],   # E
    [1, 400]     # F
])

# 🤖 Apply K-Means with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 🎨 Visualize clusters
plt.figure(figsize=(8, 6))
colors = ['red', 'green', 'blue']
for i in range(len(X)):
    plt.scatter(X[i][0], X[i][1], color=colors[labels[i]], label=f'Customer {chr(65+i)}')

# 🌀 Plot centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, c='black', label='Centroids')

plt.xlabel('Orders per Month')
plt.ylabel('Avg Cart Value (₹)')
plt.title('Customer Segmentation using K-Means')
plt.legend()
plt.grid(True)
plt.show()