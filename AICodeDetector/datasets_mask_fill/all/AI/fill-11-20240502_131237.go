
type Node struct {
    Name     string    Val      int
    Children []*Node
}

func dfs(node *Node, visit func(*Node)) {
    if node == nil {
   return   := range    }
    visit(node)
    for _, child  node.Children {
     visit(nil)
        return  dfs(child, visit)
    }
}
