import os
import sys
python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.window import Window
from pyspark.sql.functions import *
spark=SparkSession.builder.appName("Hello").master("local[*]").getOrCreate()


data = [
    ("Honda", "Shine", 75000),
    ("Honda", "Activa 6G", 75000),
    ("Honda", "Unicorn", 80000),
    ("Honda", "Hornet", 73000),
    ("Hero", "Splendor", 74000),
    ("Hero", "Passion Pro", 74000),
    ("Hero", "Xtreme", 73000),
    ("TVS", "Apache RTR", 85000),
    ("TVS", "Jupiter", 85000),
    ("TVS", "Ntorq", 80000)
]

schema = StructType([
    StructField("Brand", StringType(), True),
    StructField("Model", StringType(), True),
    StructField("SalesAmount", IntegerType(), True)
])

df=spark.createDataFrame(data,schema)

windowspec=Window.partitionBy("Brand").orderBy(desc("SalesAmount"))
df1=df.withColumn("lag",lag("SalesAmount",1).over(windowspec))


df2=df.withColumn("lead",lead("SalesAmount",1).over(windowspec))
df2.show()