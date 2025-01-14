import queue

q = queue.Queue(maxsize=4)  # 要素が３つまで入るキューを生成する

for i <extra_id_0>    <extra_id_1> # キューにデータを投入する

q.qsize()  # 3, キューに溜まった要素の数を返す
q.full()  # True, maxsize == q.qsize()のため

for <extra_id_2> range(3):
    q.get()  # 0, 1, 2の順番で取得

q.empty()  # True, キューに溜まった要素がなければTrue, なければFalse