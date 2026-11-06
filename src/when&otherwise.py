import os
import sys
python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark=SparkSession.builder.appName("Hello").master("local[*]").getOrCreate()
df =spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:\\Users\\sarat\\Desktop\\saran\\spark-course-python\\data\\AAPL.csv")

data=[(1,"saran","M",None,2000),(2,"sanjay","M","3000",4000),(3,"reshmi","F","5000",6000 )]
schema=["id","name","gender","salary","sales"]
df=spark.createDataFrame(data=data,schema=schema)

df1=df.withColumn("gender",when(df.gender=="M","Male")\
    .when(df.gender=="F","Female")\
    .otherwise(df.gender))
df1.show()
