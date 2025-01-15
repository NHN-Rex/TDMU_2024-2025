import os
import shutil
from pyspark import SparkContext

# Khởi tạo SparkContext
sc = SparkContext("local", "Twitter Data Processing")

# Đọc dữ liệu từ file CSV
lines = sc.textFile("elonmusk_tweets.csv")

# Tách các dòng thành các từ
words = lines.flatMap(lambda line: line.split(" "))

# Đếm tần số của mỗi từ
wordFrequencies = words.map(lambda word: (word.lower(), 1)).reduceByKey(lambda a, b: a + b)

# Lấy 20 từ được nhắc đến nhiều nhất
topWords = wordFrequencies.takeOrdered(20, key=lambda x: -x[1])
print("\nTop 20 words:")
for word, count in topWords:
    print(f"{word}: {count}")

# Đếm tần số của các tài khoản được nhắc đến
mentions = lines.flatMap(lambda line: [word for word in line.split() if word.startswith('@')])
mentionFrequencies = mentions.map(lambda mention: (mention, 1)).reduceByKey(lambda a, b: a + b)

# Lấy 10 tài khoản được nhắc đến nhiều nhất
topMentions = mentionFrequencies.takeOrdered(10, key=lambda x: -x[1])
print("\nTop 10 mentioned accounts:")
for account, count in topMentions:
    print(f"{account}: {count}")

# Lưu kết quả vào một tệp văn bản
savingPath = "file:///C:/spark/spark-3.5.2-bin-hadoop3/output/lab3"
if os.path.isdir(savingPath):
    shutil.rmtree(savingPath, ignore_errors=True)

wordFrequencies.saveAsTextFile(savingPath)

# Đóng SparkContext
sc.stop()
