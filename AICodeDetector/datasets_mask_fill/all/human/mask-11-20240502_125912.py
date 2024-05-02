from typing import List

list_value: List[int] = [
  <extra_id_0> 100, 23, 33, 51, 70, 32, 34, 13, 3, 79, 8, 12, 16, 134, 83]
sorted_list: List[int] = sorted(list_value)



def binary_search(sorted_list: <extra_id_1> int) -> bool:
 <extra_id_2>  """
    二分探索を実施し、検索対象の値がリスト内に含まれるかどうかの
    真偽値を取得する。

    Parameters
   <extra_id_3>    sorted_list : list of int
        ソート済みの整数値を格納したリスト。
    <extra_id_4> int
  <extra_id_5>     検索対象の値。

  <extra_id_6> Returns
    -------
    value_exists : bool
        値がリスト内に含まれるかどうか。
    <extra_id_7>   left_index: int = 0
    right_index: int = len(sorted_list) <extra_id_8>  