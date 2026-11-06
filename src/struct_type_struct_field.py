import os
import sys
python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType,ArrayType
spark=SparkSession.builder.appName("Hello").master("local[*]").getOrCreate()
data=[(1,'saran',20),(2,'Sumith',20),(3,'Snjay',21)]
schema=StructType([
    StructField("id",IntegerType(),True),
    StructField("name",StringType(),True),
    StructField("age",IntegerType(),True)
])
df=spark.createDataFrame(data,schema)

data2=[(1,[{"firstname":"saran","lastname":"lakshman"}]),(2,[{"firstname":"Sumith","lastname":"kumar"}]),(3,[{"firstname":"Sanjay","lastname":"kumar"}])]
schema2=StructType([
    StructField("id",IntegerType(),True),
    StructField("name",ArrayType(StructType([
        StructField("firstname",StringType(),True),
        StructField("lastname",StringType(),True)
    ])),True)
])
df2=spark.createDataFrame(data2,schema2)
df2.show()