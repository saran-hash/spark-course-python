import os
import sys
python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode,array, lit
spark=SparkSession.builder.appName("Hello").master("local[*]").getOrCreate()

df =spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:\\Users\\sarat\\Desktop\\saran\\spark-course-python\\data\\AAPL.csv")

df1=df.withColumn("Higher",array(lit(1),lit(2)))

df2=df1.select("Date",explode("Higher").alias("High"))
df2.show()
