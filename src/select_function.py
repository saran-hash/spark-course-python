import os
import sys
python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark=SparkSession.builder.appName("Hello").master("local[*]").getOrCreate()
df =spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:\\Users\\sarat\\Desktop\\saran\\spark-course-python\\data\\AAPL.csv")

df.select('Date','High').show()
df.select(col('Date'),col('High')).show()
columns=['Date','High']
df.select(*columns).show()
df.select(df.columns[0:3]).show()