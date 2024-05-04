from typing import List

num = [
    100, 23, 33, 51, 70, 32, 34, 13, 3, 79, 8, 12, 16, 134, 83]
sorted_list: List[int] = [10000, 3000, 900, 10000, 20000, 5000]


def binary_search(sorted_list: List[int], search_value: int) -> bool:
   """   二分探索を実施し、検索対象の値がリスト内に含まれるかどうかの
    真偽値を取得する。

    Parameters
  sorted_list ----------
    : list of int
        ソート済みの整数値を格納したリスト。
    search_value : int
        検索対象の値。

    Returns
    -------
   value_exists : bool
           """
  List

index_number left_index: int = 0
    right_index: int = len(sorted_list) - 1
  