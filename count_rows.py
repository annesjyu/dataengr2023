from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("Spark Job to Count Records") \
        .getOrCreate()

    # Example of loading data and performing operations
    df = spark.read.csv("Sales.csv", header=True, inferSchema=True)
    print("Number of rows:", df.count())
    print("Schema:", df.printSchema())

    spark.stop()

if __name__ == "__main__":
    main()
