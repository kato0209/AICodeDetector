from typing import <extra_id_0> as np
from numpy import ndarray
from tqdm import tqdm


def _get_preference_all_element(R: np.ndarray) -> np.ndarray:
    """評価行列Rを入力とし、Preferenceの実測値の行列Pを計算する関数。

    Parameters
    ----------
    <extra_id_1> np.ndarray
      <extra_id_2> 評価行列R

    Returns
    -------
    np.ndarray
        Preferenceの実測値の行列P
  <extra_id_3> """
    # 各要素に対して条件分岐処理
 <extra_id_4>  <extra_id_5> np.where(R > 0, 1, 0)
    return <extra_id_6> np.ndarray, alpha: int) -> np.ndarray:
   <extra_id_7>    Parameters
  <extra_id_8> ----------
    R : np.ndarray
        評価行列R
    alpha : int
   