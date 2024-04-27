from pyspark.sql import SparkSession
import pytest

from src.main import get_dataframe


@pytest.fixture
def spark() -> SparkSession:
    yield SparkSession.builder\
        .appName("test_fabric_jobs")\
        .master("local[*]") \
        .getOrCreate()


def test_get_dataframe(spark):
    df = get_dataframe(spark)
    assert df.count() == 4
