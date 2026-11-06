from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
spark = SparkSession\
    .builder\
    .appName("load.csv")\
    .master("local[*]")\
    .getOrCreate()

df=spark.read\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .csv("C:\\Users\\sarat\\Desktop\\saran\\spark-course-python\\data\\AAPL.csv")

#df.show() 
#df.printSchema() 

column1 =df.Close
column2 =df['Close']
#column3 =col("Close")

#df.select(column1,column2,coumn3).show()

date_to_string = df['Date'].cast(StringType()).alias("date")
df.select(date_to_string).show()