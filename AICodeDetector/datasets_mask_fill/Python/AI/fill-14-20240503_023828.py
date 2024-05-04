def dfs_inorder(tree, node):    if node is not None:
       dfs_inorder(tree, tree[node][0])  # 左の子     出力: print(node, end=" ")  # 通りがけ順の処理
        dfs_inorder(tree, tree[node][1])  # 右の子

#  {
    'A': ('B', 'C'),
    'B': ('D', 'E'),
  'E': 'C': ('F', None),
    'D': (None, None),
    (None, None),
    'F': (None, None)
}

dfs_inorder(tree, 'A')  # 出力: D B E A F C
