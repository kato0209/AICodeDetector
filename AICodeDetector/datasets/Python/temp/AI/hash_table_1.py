class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        hash_index = self._hash(key)
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                self.table[hash_index][i] = (key, value)
                return
        self.table[hash_index].append((key, value))

    def get(self, key):
        hash_index = self._hash(key)
        for k, v in self.table[hash_index]:
            if k == key:
                return v
        return None

# ハッシュテーブルのインスタンスを作成
hash_table = HashTable()

# いくつかのキーと値を追加
hash_table.put("key1", "value1")
hash_table.put("key2", "value2")
hash_table.put("key3", "value3")

# キーに対応する値を取得
value1 = hash_table.get("key1")
value2 = hash_table.get("key2")
value3 = hash_table.get("key3")

value1, value2, value3

