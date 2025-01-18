import pandas as pd
import numpy as np
from pyspark.ml.clustering import KMeans
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler

# Khởi tạo Spark Session
spark = SparkSession.builder.appName("Distributed KMeans Example").getOrCreate()

# Đọc dữ liệu iris vào Spark DataFrame
iris_data = spark.createDataFrame(pd.read_csv('E:/TTNT/2024-2025/Bigdata/lab4/iris.csv',
                                               header=0, names=['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'label']))
print("First 10 rows:")
iris_data.show(10)

# Tạo vector đặc trưng từ DataFrame
# 
assembler = VectorAssembler(inputCols=["sepal-length", "sepal-width", "petal-length", "petal-width"], outputCol="features")
irisFeatures = assembler.transform(iris_data)
irisFeatures.show(5)





# Huấn luyện mô hình K-means với K=3
kmeans = KMeans().setK(3).setSeed(0)
model = kmeans.fit(irisFeatures)

# In ra tâm điểm của các cụm
centers = model.clusterCenters()
np.set_printoptions(precision=2)
print("Centers learned by Spark ML: ")
for center in centers:
    print(center)

# Đóng Spark Session
spark.stop()
