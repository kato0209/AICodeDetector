func (n *Node) DFS(name string) *Node {
	stack := []*Node{n}
	for len(stack) > 0 {
		current := stack[len(stack)-1]
		stack <extra_id_0> current.Name == name {
			return current
		}
		for _, child <extra_id_1> current.Children {
			stack = append(stack, child)
		}
	}
	return nil
}
