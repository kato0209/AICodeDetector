#!/usr/bin/env python3

import sys

# <extra_id_0>  arr   : 数値リスト
#   n  <extra_id_1> : 要素数
#   i    : 探索する要素の位置
# <extra_id_2> 探索値

arr = [40, <extra_id_3> 50, 20]
n = len(arr)

print(arr)

# 探索する値を入力
target = input('探索値を入力する。: ')
target = int(target)    # 文字列から数値に変換

# 探索する(リニアサーチ)
i = 0

while i < n:
    if arr[i] == target:
        <extra_id_4> は0から数えて {i} 番目にあります。')
        sys.exit()

    i += <extra_id_5> は見つかりませんでした。')
