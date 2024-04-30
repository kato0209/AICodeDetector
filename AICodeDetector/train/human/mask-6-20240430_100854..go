func (n *Node) DFS(name string) *Node {
	stack := []*Node{n}
	for len(stack) > 0 {
		current <extra_id_0> = stack[:len(stack)-1]
		if current.Name == name <extra_id_1> _, child := range current.Children {
			stack = append(stack, child)
		}
	}
	return nil
}
