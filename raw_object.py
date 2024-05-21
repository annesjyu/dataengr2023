from pyspark.sql import Row
from pyspark.sql import SparkSession

spark = (SparkSession.builder.appName("schema_example").getOrCreate())   # Create a SparkSession

# Define rows
row1 = Row("Matei Zaharia", "CA")
row2 = Row("Reynold Xin", "CA")
rows = [row1, row2]

print(type(row1))

# Create DataFrame from rows
authors_df = spark.createDataFrame(rows, ["Authors", "State"])

print(type(authors_df))

print(authors_df.show())
