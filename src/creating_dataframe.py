
import os
import sys
python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Hello").master("local[*]").getOrCreate()

data=[(1,'saran',20),(2,'Sumith',20),(3,'Snjay',21)]
schema=['id','name','age']

df=spark.createDataFrame(data, schema)
df.show()
