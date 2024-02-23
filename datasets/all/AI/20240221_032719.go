
package main

import (
	"fmt"
)

// Implementing depth-first search algorithm

type Graph struct {
	Vertices map[int][]int
}

func (g *Graph) DFS(v int, visited map[int]bool) {
	visited[v] = true
	fmt.Println("Visited vertex:", v)

	for _, u := range g.Vertices[v] {
		if !visited[u] {
			g.DFS(u, visited)
		}
	}
}

func main() {
	graph := Graph{
		Vertices: map[int][]int{
			0: {1, 2},
			1: {2},
			2: {0, 3},
			3: {3},
		},
	}

	visited := make(map[int]bool)
	startingVertex := 2
	fmt.Println("Starting DFS from vertex:", startingVertex)
	graph.DFS(startingVertex, visited)
}
