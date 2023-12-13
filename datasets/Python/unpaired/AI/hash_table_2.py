class LinearProbingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        hash_index = self._hash(key)

        # キーがすでに存在する場合は値を更新
        if self.keys[hash_index] == key:
            self.values[hash_index] = value
            return

        # コリジョンが発生した場合は線形探索で空きスロットを探す
        original_hash = hash_index
        while self.keys[hash_index] is not None:
            hash_index = (hash_index + 1) % self.size
            if hash_index == original_hash:  # テーブルが満杯の場合
                raise Exception("Hash table is full")

        # 新しいキーと値を設定
        self.keys[hash_index] = key
        self.values[hash_index] = value

    def get(self, key):
        hash_index = self._hash(key)

        # キーに対応する値を探す
        original_hash = hash_index
        while self.keys[hash_index] is not None:
            if self.keys[hash_index] == key:
                return self.values[hash_index]
            hash_index = (hash_index + 1) % self.size
            if hash_index == original_hash:  # 全て探索して見つからなかった場合
                return None

        return None

# ハッシュテーブルのインスタンスを作成
linear_hash_table = LinearProbingHashTable()

# いくつかのキーと値を追加
linear_hash_table.put("key1", "value1")
linear_hash_table.put("key2", "value2")
linear_hash_table.put("key3", "value3")

# キーに対応する値を取得
value1 = linear_hash_table.get("key1")
value2 = linear_hash_table.get("key2")
value3 = linear_hash_table.get("key3")

value1, value2, value3

