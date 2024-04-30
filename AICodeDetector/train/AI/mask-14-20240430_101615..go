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
func NewGraph(vertices <extra_id_0> {
	return &Graph{
		vertices: vertices,
		adjList:  make(map[int][]int),
	}
}

// AddEdge <extra_id_1> edge to the graph.
func (g *Graph) <extra_id_2> int) {
	g.adjList[u] = append(g.adjList[u], v) // Directed graph
}

// DFSUtil is a <extra_id_3> that helps to perform DFS recursively.
func (g *Graph) DFSUtil(v int, visited map[int]bool) <extra_id_4> true
	fmt.Printf("Visited %d\n", v)

	for _, i := range <extra_id_5> !visited[i] {
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
	graph.AddEdge(0, <extra_id_6> 3)
	graph.AddEdge(1, <extra_id_7> 4)

	fmt.Println("Depth-First Search starting from vertex 0:")
	graph.DFS(0)
}
