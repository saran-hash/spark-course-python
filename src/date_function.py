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
    ("B001", "Arjun", "2024-01-05", "2024-01-08"),
    ("B002", "Meena", "2024-01-07", "2024-01-10"),
    ("B003", "Ravi", "2024-01-10", "2024-01-15"),
    ("B004", "Suma", "2024-01-12", "2024-01-13"),
    ("B005", "Karan", "2024-01-15", "2024-01-20")
]

df = spark.createDataFrame(
    data,
    ["OrderID", "CustomerName", "PurchaseDate", "DeliveryDate"]
)

df1=df.withColumn("deliverydatecount",datediff(col("DeliveryDate"),col("PurchaseDate")))
df1.show()
current_date =df.withColumn("current_date", current_date())
monthsbt=df.withColumn("monthsbt", months_between(col("DeliveryDate"), col("PurchaseDate")))
monthsbt.show()