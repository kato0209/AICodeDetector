package main

import (
	"fmt"
)

// Graph represents a graph with an adjacency list.
type Graph struct {
	vertices int
	adjList  <extra_id_0> creates a new <extra_id_1> int) *Graph {
	return &Graph{
		vertices: <extra_id_2> make(map[int][]int),
	}
}

// AddEdge adds an edge <extra_id_3> graph.
func (g *Graph) AddEdge(u, v int) {
	g.adjList[u] = append(g.adjList[u], v)
}

// BFS performs a breadth-first search starting from vertex v.
func (g *Graph) BFS(start int) <extra_id_4> make(map[int]bool)
	queue := []int{start}

	for len(queue) > 0 {
		vertex := queue[0]
		queue = queue[1:]
		if !visited[vertex] {
			fmt.Printf("Visited %d\n", vertex)
			visited[vertex] = true
			for _, <extra_id_5> range <extra_id_6> !visited[adjacent] {
					queue = append(queue, adjacent)
				}
			}
		}
	}
}

func main() {
	graph := NewGraph(5)
	graph.AddEdge(0, 1)
	graph.AddEdge(0, 2)
	graph.AddEdge(1, 3)
	graph.AddEdge(1, 4)
	graph.AddEdge(2, 3)
	graph.AddEdge(3, 4)

	fmt.Println("Breadth-First Search starting from vertex 0:")
	graph.BFS(0)
}
