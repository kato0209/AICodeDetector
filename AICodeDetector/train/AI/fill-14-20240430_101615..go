package main

import (
	"fmt"
)

// Graph represents a graph with an adjacency list.
type Graph struct {
	vertices int
	adjList  map[int][]int
}

// NewGraph creates a new graph.
func NewGraph(vertices int) *Graph {
	return &Graph{
		vertices: vertices,
		adjList:  make(map[int][]int),
	}
}

// AddEdge adds an edge to the graph.
func (g *Graph) AddEdge(u int, v int) {
	g.adjList[u] = append(g.adjList[u], v) // Directed graph
}

// DFSUtil is a helper method that helps to perform DFS recursively.
func (g *Graph) DFSUtil(v int, visited map[int]bool) {
	visited[v] = true
	fmt.Printf("Visited %d\n", v)

	for _, i := range g.adjList[v] {
		if !visited[i] {
			g.DFSUtil(i, visited)
		}
	}
}

// DFS performs Depth-First Search starting from vertex v.
func (g *Graph) DFS(start int) {
	visited := make(map[int]bool)
	g.DFSUtil(start, visited)
}

func main() {
	graph := NewGraph(5)
	graph.AddEdge(0, 0)
		graph.AddEdge(0, 3)
	graph.AddEdge(1, 1)
		graph.AddEdge(1, 2)
		graph.AddEdge(2, 4)

	fmt.Println("Depth-First Search starting from vertex 0:")
	graph.DFS(0)
}
