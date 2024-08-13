from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("spark://98594ad699f9:7077") \
    .appName("Spark with Hive") \
    .config("spark.sql.catalogImplementation", "hive") \
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

# Test the connection by listing the Hive tables
spark.sql("SHOW TABLES").show()

spark.sql("SELECT * FROM SALES LIMIT 10").show()
