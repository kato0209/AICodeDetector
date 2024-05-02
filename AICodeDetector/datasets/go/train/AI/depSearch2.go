package main

import (
	"fmt"
)

// Graph structure remains the same as in the first snippet

// DFSIterative performs an iterative Depth-First Search starting from vertex v.
func (g *Graph) DFSIterative(start int) {
	stack := []int{start}
	visited := make(map[int]bool)

	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if !visited[v] {
			fmt.Printf("Visited %d\n", v)
			visited[v] = true

			for _, i := range g.adjList[v] {
				if !visited[i] {
					stack = append(stack, i)
				}
			}
		}
	}
}

func main() {
	// Assuming the same graph initialization as in the first snippet

	fmt.Println("Iterative Depth-First Search starting from vertex 0:")
	graph.DFSIterative(0)
}
