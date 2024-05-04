def <extra_id_0>    if node is not None:
       <extra_id_1> tree[node][0])  # <extra_id_2>     <extra_id_3> print(node, end=" ")  # 通りがけ順の処理
        dfs_inorder(tree, tree[node][1])  # 右の子

# <extra_id_4> {
    'A': ('B', 'C'),
    'B': ('D', 'E'),
  <extra_id_5> 'C': ('F', None),
    'D': (None, None),
   <extra_id_6> (None, None),
    'F': (None, None)
}

dfs_inorder(tree, 'A')  # 出力: D B E A F C
