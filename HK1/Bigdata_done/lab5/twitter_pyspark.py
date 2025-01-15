import sys
import io

# Thiết lập mã hóa đầu ra là UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, split

# Khởi tạo Spark Session
spark = SparkSession.builder.appName("Twitter Analysis").getOrCreate()

# Đọc dữ liệu từ file
df = spark.read.text('Twitter_followings.txt')

# Chia dữ liệu thành hai cột user_id1 và user_id2
df = df.withColumn('user_id1', split(df['value'], ' ')[0]) \
       .withColumn('user_id2', split(df['value'], ' ')[1]) \
       .drop('value')

# Thống kê số lượng người theo dõi cho mỗi tài khoản
followers_count_df = df.groupBy('user_id2').agg(count('user_id1').alias('followers_count'))

# Liệt kê top 5 người dùng có nhiều theo dõi nhất
top_followers_df = followers_count_df.orderBy(col('followers_count').desc()).limit(5)
print("Top 5 nguoi dung co nhieu theo doi nhat:")
top_followers_df.show()

# Tìm cặp tài khoản theo dõi lẫn nhau
mutual_followers_df = df.alias('a').join(df.alias('b'),
    (col('a.user_id1') == col('b.user_id2')) & (col('a.user_id2') == col('b.user_id1')),
    'inner').select(col('a.user_id1').alias('user1'), col('a.user_id2').alias('user2'))

# Liệt kê các cặp tài khoản theo dõi lẫn nhau
print('Cac cap tai khoan theo doi lan nhau:')
mutual_followers_df.show(truncate=False)

# Dừng Spark Session
spark.stop()
