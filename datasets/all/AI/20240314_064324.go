
type Node struct {
    Val      int
    Children []*Node
}

func dfs(node *Node, visit func(*Node)) {
    if node == nil {
        return
    }
    visit(node)
    for _, child := range node.Children {
        dfs(child, visit)
    }
}
