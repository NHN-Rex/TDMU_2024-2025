import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Nạp dữ liệu
iris_data = pd.read_csv('E:/TTNT/2024-2025/Bigdata/lab4/iris.csv', header=None, names=['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'label'])

# Tạo vector đặc trưng
X = iris_data[['sepal-length', 'sepal-width', 'petal-length', 'petal-width']].values

# Huấn luyện mô hình K-means với K=3
kmeans_sklearn = KMeans(n_clusters=3, random_state=0)
kmeans_sklearn.fit(X)

# In ra tâm điểm của các cụm
centers_sklearn = kmeans_sklearn.cluster_centers_
np.set_printoptions(precision=2)
print("Centers learned by Scikit-learn: ")
for center in centers_sklearn:
    print(center)

# Vẽ biểu đồ các cụm
plt.scatter(X[:, 0], X[:, 1], c=kmeans_sklearn.labels_, cmap='viridis', marker='o')
plt.scatter(centers_sklearn[:, 0], centers_sklearn[:, 1], c='red', s=200, alpha=0.75, label='Centroids')
plt.title('K-means Clustering (Scikit-learn)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
