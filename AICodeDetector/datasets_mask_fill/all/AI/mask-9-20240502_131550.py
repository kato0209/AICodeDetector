def dfs_inorder(tree, node):
    if node is not None:
      <extra_id_0> dfs_inorder(tree, tree[node][0])  # 左の子
        print(node, end=" ")  # 通りがけ順の処理
       <extra_id_1> tree[node][1])  # 右の子

# バイナリツリーの例
tree = {
  <extra_id_2> 'A': ('B', 'C'),
    'B': ('D', <extra_id_3>   <extra_id_4> None),
    'D': (None, None),
  <extra_id_5> 'E': (None, None),
    <extra_id_6> None)
}

dfs_inorder(tree, 'A')  # 出力: D B E A F C
