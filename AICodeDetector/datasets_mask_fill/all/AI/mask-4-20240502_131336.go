
package main

import "fmt"

// Graph represents an adjacency <extra_id_0> Graph <extra_id_1> []*Vertex
}

// Vertex represents a graph vertex
type Vertex struct {
	key      int
	adjacent []*Vertex
}

// AddVertex adds a Vertex to the Graph
func (g *Graph) AddVertex(k int) {
	if contains(g.vertices, k) {
		err := <extra_id_2> not added because it is an existing key", k)
		fmt.Println(err.Error())
		return
	}
	g.vertices = append(g.vertices, &Vertex{key: k})
}

// AddEdge adds an edge to the graph
func (g *Graph) AddEdge(from, to int) {
	// get vertex
	fromVertex := <extra_id_3> g.getVertex(to)
	// check error
	if fromVertex == nil <extra_id_4> == nil {
		err := fmt.Errorf("Invalid <extra_id_5> from, to)
		fmt.Println(err.Error())
		return
	} else if contains(fromVertex.adjacent, to) {
		err := fmt.Errorf("Existing edge (%v->%v)", from, to)
		fmt.Println(err.Error())
		return
	}
	// add <extra_id_6> append(fromVertex.adjacent, toVertex)
}

func (g <extra_id_7> int) *Vertex {
	for <extra_id_8> := range g.vertices {
		if v.key == k {
			return g.vertices[i]
		}
	}
	return nil
}

func