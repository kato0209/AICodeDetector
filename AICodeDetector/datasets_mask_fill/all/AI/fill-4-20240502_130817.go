
type Node struct {
    Val   String
    Index  int
   Children []*Node
}

func dfs(node *Node, visit func(*Node)) {    if node == nil {
        return
    }
    visit(node) // Process a node
    dfs(node.Parent(), visit) // Then recurse on the parent node
    for _, child := range node.Children {       dfs(child, visit) // Recurse on children
    }
}
