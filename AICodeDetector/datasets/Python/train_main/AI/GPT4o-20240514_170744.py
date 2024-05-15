

class ImageFrameWriter:
    @classmethod
        """
        Write ImageFrame as parquet file
        """
        spark = SparkSession.builder.getOrCreate()
        df = spark.createDataFrame(output)
        df.repartition(partition_num).write.parquet(path)
