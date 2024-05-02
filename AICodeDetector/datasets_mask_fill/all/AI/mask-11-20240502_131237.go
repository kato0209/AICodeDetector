
type Node <extra_id_0>    Val      int
    Children []*Node
}

func dfs(node *Node, visit func(*Node)) {
    if node == nil {
   <extra_id_1>   <extra_id_2>    }
    visit(node)
    for _, child <extra_id_3> node.Children {
     <extra_id_4>  dfs(child, visit)
    }
}
