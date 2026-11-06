import os
import sys
python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark=SparkSession.builder.appName("Hello").master("local[*]").getOrCreate()
df =spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:\\Users\\sarat\\Desktop\\saran\\spark-course-python\\data\\AAPL.csv")

data1=[(1,'saran',20),(2,'sanjay',21)]
data2=[("siva",3,20,"AIML"),("vels",4,21,"AIDS")]

schema1=["id","name","age"]
schema2=["name","id","age","dept"]

df1=spark.createDataFrame(data=data1,schema=schema1)
df2=spark.createDataFrame(data=data2,schema=schema2)
df1.show()
df2.show()

df3=df1.unionByName(df2,allowMissingColumns=True)
df3.show()