#!/usr/bin/env python3

import sys

# 線形探索法(linear search:リニアサーチ)

# <extra_id_0>   : 数値リスト
#   n    : 要素数
#   <extra_id_1>   : 探索する要素の位置
# target : 探索値

arr = [40, 10, 30, 50, 20]
n <extra_id_2> 探索する値を入力
target = input('探索値を入力する。: ')
target <extra_id_3>    # <extra_id_4> = <extra_id_5> < n:
    if arr[i] == target:
        print(f'探索値: {target} は0から数えて {i} 番目にあります。')
        sys.exit()

    i += 1

print(f'探索値: {target} は見つかりませんでした。')
