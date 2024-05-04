import queue

q = queue.Queue(maxsize=4)  # 要素が３つまで入るキューを生成する

for i in range(3):
    q.put(i)  # キューにデータを投入する

q.qsize()  # 3, <extra_id_0> # True, maxsize == q.qsize()のため

for _ in range(3):
   <extra_id_1>  # 0, <extra_id_2>  # True, キューに溜まった要素がなければTrue, なければFalse