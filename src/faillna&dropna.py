import os
import sys
python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark=SparkSession.builder.appName("Hello").master("local[*]").getOrCreate()
df =spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:\\Users\\sarat\\Desktop\\saran\\spark-course-python\\data\\AAPL.csv")

data=[(1,'saran',None),(2,'sanjay',18),(3,'None',None)]

schema=['id','name','age']
df=spark.createDataFrame(data=data,schema=schema)
df1=df.fillna(value=20,subset=['age'])\
    .fillna(value='Unknown',subset=['name'])


df2=df.dropna(how='any')
df2.show()

df3=df.dropna(how='all')
df3.show()
