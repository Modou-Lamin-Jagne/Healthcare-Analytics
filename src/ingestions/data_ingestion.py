import pandas as pd
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("HealthcareDataIngestion").getOrCreate()

# Load data from CSV
data = pd.read_csv("../../data/raw/healthcare_data.csv")

# Convert to Spark DataFrame
df = spark.createDataFrame(data)

# Write data to HDFS
df.write.format("parquet").save("hdfs://namenode:8020/user/hadoop/healthcare_data")
