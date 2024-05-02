
package main

import "fmt"

// Graph represents an adjacency list graph
type Graph struct {
	vertices []*Vertex
}

// Vertex represents a graph vertex
type Vertex struct {
	key      int
	adjacent []*Vertex
}

// AddVertex adds a Vertex to the Graph
func (g *Graph) AddVertex(k int) {
	if contains(g.vertices, k) {
		err := fmt.Errorf("Vertex %v not added because it is an existing key", k)
		fmt.Println(err.Error())
		return
	}
	g.vertices = append(g.vertices, &Vertex{key: k})
}

// AddEdge adds an edge to the graph
func (g *Graph) AddEdge(from, to int) {
	// get vertex
	fromVertex := g.getVertex(from)
	toVertex := g.getVertex(to)
	// check error
	if fromVertex == nil || toVertex == nil {
		err := fmt.Errorf("Invalid edge (%v->%v)", from, to)
		fmt.Println(err.Error())
		return
	} else if contains(fromVertex.adjacent, to) {
		err := fmt.Errorf("Existing edge (%v->%v)", from, to)
		fmt.Println(err.Error())
		return
	}
	// add edge
	fromVertex.adjacent = append(fromVertex.adjacent, toVertex)
}

func (g *Graph) getVertex(k int) *Vertex {
	for i, v := range g.vertices {
		if v.key == k {
			return g.vertices[i]
		}
	}
	return nil
}

func contains(s []*Vertex, k int) bool {
	for _, v := range s {
		if k == v.key {
			return true
		}
	}
	return false
}

func (g *Graph) BreadthFirstSearch(start int) {
	startVertex := g.getVertex(start)
	if startVertex == nil {
		fmt.Println("Start vertex not found!")
		return
	}

	visited := make(map[int]bool)
	queue := make([]*Vertex, 0)

	queue = append(queue, startVertex)

	for len(queue) > 0 {
		currentVertex := queue[0]
		queue = queue[1:]

		visited[currentVertex.key] = true
		fmt.Println(currentVertex.key)

		for _, adjVertex := range currentVertex.adjacent {
			if !visited[adjVertex.key] {
				queue = append(queue, adjVertex)
				visited[adjVertex.key] = true
			}
		}
	}
}

func main() {
	// Example usage
	graph := Graph{}
	for i := 1; i <= 5; i++ {
		graph.AddVertex(i)
	}

	graph.AddEdge(1, 2)
	graph.AddEdge(1, 3)
	graph.AddEdge(2, 4)
	graph.AddEdge(3, 5)
	graph.AddEdge(4, 5)

	fmt.Println("Breadth First Search: Starting from vertex 1")
	graph.BreadthFirstSearch(1)
}
