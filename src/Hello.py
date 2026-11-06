from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Hello").master("local[*]").getOrCreate()
print(spark.version)
