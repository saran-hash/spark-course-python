import os
import sys
python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark=SparkSession.builder.appName("Hello").master("local[*]").getOrCreate()
df =spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:\\Users\\sarat\\Desktop\\saran\\spark-course-python\\data\\AAPL.csv")

df1=df.collect()
print(df1[0][5])
print(df1[1])
