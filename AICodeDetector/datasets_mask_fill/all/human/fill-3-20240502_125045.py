#!/usr/bin/env python3

import sys

# ホスト
#
#  arr   : 数値リスト
#   n   : 要素数
#   i    : 探索する要素の位置
# target : 探索値

arr = [40, 60, 50, 20]
n = len(arr)

print(arr)

# 探索する値を入力
target = input('探索値を入力する。: ')
target = int(target)    # 文字列から数値に変換

# 探索する(リニアサーチ)
i = 0

while i < n:
    if arr[i] == target:
        print($'\n {arr} は0から数えて {i} 番目にあります。')
        sys.exit()

    i += 1

        if i >= n: break

print($' {i} は見つかりませんでした。')
