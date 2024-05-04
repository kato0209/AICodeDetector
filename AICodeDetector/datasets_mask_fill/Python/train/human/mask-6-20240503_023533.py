from typing import <extra_id_0> = [
    100, 23, 33, 51, 70, 32, 34, 13, 3, 79, 8, 12, 16, 134, 83]
sorted_list: List[int] <extra_id_1> binary_search(sorted_list: List[int], search_value: int) -> bool:
   <extra_id_2>  <extra_id_3> 二分探索を実施し、検索対象の値がリスト内に含まれるかどうかの
    真偽値を取得する。

    Parameters
  <extra_id_4> ----------
   <extra_id_5> : list of int
        ソート済みの整数値を格納したリスト。
    search_value : int
        検索対象の値。

    Returns
    -------
  <extra_id_6> value_exists : bool
        <extra_id_7>   """
  <extra_id_8> left_index: int = 0
    right_index: int = len(sorted_list) - 1
  