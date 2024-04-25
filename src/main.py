import logging

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

logging.basicConfig(format='%(levelname)s - %(name)s - %(asctime)s\n%(message)s', level=logging.INFO)
logger = logging.getLogger("src.main")


def get_dataframe(spark: SparkSession) -> DataFrame:
    schema = StructType([
        StructField('id', IntegerType(), True),
        StructField('first_name', StringType(), True),
        StructField('last_name', StringType(), True)
    ])

    data = [
        (1, "Thibauld", "Croonenborghs"),
        (2, "Dionys", "Nabarro"),
        (3, "Koen", "Verbeeck"),
    ]

    return spark.createDataFrame(schema=schema, data=data)


if __name__ == '__main__':
    spark = SparkSession.builder.appName("revenue_aggregates").getOrCreate()
    df = get_dataframe(spark)
    logger.info(f"The dataframe contains {df.count()} records.")
