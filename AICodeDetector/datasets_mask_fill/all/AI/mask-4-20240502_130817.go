
type Node struct {
    Val   <extra_id_0>  int
   <extra_id_1> []*Node
}

func dfs(node *Node, visit <extra_id_2>    if node == nil {
        return
    }
    visit(node) // Process <extra_id_3> node
    for <extra_id_4> := range node.Children <extra_id_5>       dfs(child, visit) // Recurse on children
    }
}
