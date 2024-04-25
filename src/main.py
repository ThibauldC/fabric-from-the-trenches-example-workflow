import logging

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

logging.basicConfig(format='%(levelname)s - %(name)s - %(asctime)s\n%(message)s', level=logging.INFO)
logger = logging.getLogger("src.main")


def count_dataframe(df: DataFrame) -> int:
    return df.count()


def test_function(spark: SparkSession):
    schema = StructType([
        StructField('id', IntegerType(), True),
        StructField('first_name', StringType(), True),
        StructField('last_name', StringType(), True)
    ])

    data = [
        (1, "Thibauld", "Croonenborghs"),
        (2, "Dionys", "Nabarro")
    ]

    df = spark.createDataFrame(schema=schema, data=data)
    count = count_dataframe(df)
    logger.info(f"The dataframe contains {count} records.")


if __name__ == '__main__':
    spark = SparkSession.builder.appName("revenue_aggregates").getOrCreate()
    test_function(spark)
