
package main

import "fmt"

// Graph represents an adjacency graph of vertices
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
		err := fmt.Errorf("Vertex (%v) not added because it is an existing key", k)
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
		err := fmt.Errorf("Invalid edge from (%v->%v)", from, to)
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

func