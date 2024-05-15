
    """ Return a JavaRDD of Object by unpickling

    It will convert each Python object into Java object by Pyrolite, whenever
    the RDD is serialized in batch or not.
    """
    
    # Ensure the RDD is serialized with BatchedSerializer
    ser = BatchedSerializer(PickleSerializer(), batchSize=10)
    