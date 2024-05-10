
    rdd = rdd._reserialize(AutoBatchedSerializer(PickleSerializer()))
    return rdd.ctx._jvm.SerDeUtil.pythonToJava(rdd._jrdd, True)


class AutoBatchedSerializer(PickleSerializer):

    def dumps(self, obj):
        return pickle.dumps(obj, 2)

    def loads(self, obj):
        return pickle.loads(obj)


class BatchedSerializer(PickleSerializer):

    def __init__(self, batched_serializer, reducers=None):
        self.batched_serializer = batched_serializer
        self.red