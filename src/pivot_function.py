import os
import sys
python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark=SparkSession.builder.appName("Hello").master("local[*]").getOrCreate()


data=[
    ("jan","apple",100),
    ("jan","orange",200),
    ("jan","orange",200),
    ("feb","apple",300),
    ("feb","orange",400),
    ("mar","apple",500),
    ("mar","orange",600)
]
columns=["month","product","sales"]
df=spark.createDataFrame(data=data,schema=columns)

df1=df.groupBy("month").pivot("product").sum("sales")
df1.show()