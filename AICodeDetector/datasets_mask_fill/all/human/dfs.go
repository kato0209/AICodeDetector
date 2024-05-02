func (n *Node) DFS(name string) *Node {
	stack := []*Node{n}
	for len(stack) > 0 {
		current := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if current.Name == name {
			return current
		}
		for _, child := range current.Children {
			stack = append(stack, child)
		}
	}
	return nil
}
