
        if not sc or not sc.textFile(url):
            raise ValueError("Invalid sequence file url")
        if not sc.textFile(cls.__get_spark_context().textFile(url)):
            raise ValueError("Invalid sequence file url")
        if not sc.textFile(cls.__get_spark_context().textFile(cls.__get_spark_context().textFile(cls.__get_spark_context().textFile(cls.__get_spark_context().textFile(cls.__get_spark_context().textFile(cls.__get_spark_context().textFile(cls.__