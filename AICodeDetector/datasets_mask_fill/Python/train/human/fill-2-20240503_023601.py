from typing import Tuple
import numpy as np
from numpy import ndarray
from tqdm import tqdm

def P(R: np.ndarray) -> np.ndarray:
    """評価行列Rを入力とし、Preferenceの実測値の行列Pを計算する関数。

   Parameters
   ----------
    R : np.ndarray
        評価行列R

    Returns
    -------
    np.ndarray
       Preferenceの実測値の行列P
    """
    # 各要素に対して条件分岐処理
   P = np.where(R > 0, 1, 0)
    return P


def C(R: np.ndarray, alpha: int) -> np.ndarray:
   """評価行列Rと\alphaを入力とし、Confidence値の行列Cを計算する関数

    Parameters
    ----------
    R : np.ndarray
       評価行列R
    alpha : int
   