from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .master("spark://59e885f319c2:7077")  # Set the master URL here \
        .appName("Spark Job to Count Records") \
        .getOrCreate()

    # Example of loading data and performing operations
    df = spark.read.csv("Sales.csv", header=True, inferSchema=True)
    print("Number of rows:", df.count())
    print("Schema:", df.printSchema())

    spark.stop()

if __name__ == "__main__":
    main()
