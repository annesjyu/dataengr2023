from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.master('spark://59e885f319c2:7077').appName('Spark Job to Count Records').getOrCreate()

    # Example of loading data and performing operations
    df = spark.read.csv('Sales.csv', header=True, inferSchema=True)
    print('Number of rows:', df.count())
    spark.stop()

if __name__ == '__main__':
    main()
