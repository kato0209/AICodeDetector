package main

import (
	"fmt"
)

// Graph structure remains the same as in the <extra_id_0> DFSIterative performs an iterative Depth-First Search starting from vertex <extra_id_1> *Graph) DFSIterative(start int) {
	stack <extra_id_2> := make(map[int]bool)

	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if !visited[v] {
			fmt.Printf("Visited <extra_id_3> = true

			for _, i := range g.adjList[v] {
				if !visited[i] {
					stack = append(stack, i)
				}
			}
		}
	}
}

func main() {
	// Assuming the same graph initialization as <extra_id_4> first snippet

	fmt.Println("Iterative Depth-First Search starting from vertex 0:")
	graph.DFSIterative(0)
}
