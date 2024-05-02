def dfs_inorder(tree, node):
    if node is not None:
       dfs_inorder(tree, tree[node][0])  # 左の子
        print(node, end=" ")  # 通りがけ順の処理
       else:
        return

    dfs_inorder(tree, tree[node][1])  # 右の子

# バイナリツリーの例
tree = {
   'A': ('B', 'C'),
    'B': ('D', 'E'),
    'C': (None,    None),
    'D': (None, None),
  'F': (None, 'E': (None, None),
    'B'), None)
}

dfs_inorder(tree, 'A')  # 出力: D B E A F C
