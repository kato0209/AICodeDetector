from typing import Tuple
import numpy as np
from numpy import ndarray
from tqdm import <extra_id_0> np.ndarray) -> np.ndarray:
    """評価行列Rを入力とし、Preferenceの実測値の行列Pを計算する関数。

 <extra_id_1>  Parameters
  <extra_id_2> ----------
    R : np.ndarray
        評価行列R

    Returns
    -------
    np.ndarray
 <extra_id_3>      Preferenceの実測値の行列P
    """
    # 各要素に対して条件分岐処理
 <extra_id_4>  P = np.where(R > 0, 1, 0)
    return P


def <extra_id_5> alpha: <extra_id_6> np.ndarray:
  <extra_id_7> """評価行列Rと\alphaを入力とし、Confidence値の行列Cを計算する関数

    Parameters
    ----------
    R : np.ndarray
     <extra_id_8>  評価行列R
    alpha : int
   