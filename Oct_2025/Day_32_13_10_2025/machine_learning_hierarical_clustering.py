from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from  scipy.cluster.hierarchy import  dendrogram, linkage



iris = load_iris()
data = iris.data
feature_name = iris.feature_names
# print(feature_name)
# print(data)


model = AgglomerativeClustering(n_clusters=3,linkage='single', metric='euclidean')
model.fit(data)

labels = model.labels_
print(labels)



target_names = iris.target_names
target = iris. target
import numpy as np
actual_target_data = np.array([target_names[i] for i in target]) #target indicates the target names

results_df = pd. DataFrame({
    'actual_target': actual_target_data,
    'cluster_label': labels
})

# 4. Create a cross-tabulation to see the relationship
cross_tab = pd.crosstab(results_df['actual_target'], results_df['cluster_label' ])

# 5. Interpret the cross-tabulation
print("Cross-tabulation of actual_target vs. Cluster Labels:")
print(cross_tab)
print("nMapping clusters to known categories:")

# Find the dominant ground truth category for each cluster label
for cluster_id in cross_tab.columns:
    dominant_category = cross_tab[cluster_id].idxmax()
    count = cross_tab[cluster_id].max()
    print(f"Cluster {cluster_id} likely corresponds to '{dominant_category}' ({count} samples)")