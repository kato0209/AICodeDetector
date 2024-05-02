
package main

import (
	"fmt"
	"math"
)

// Define a structure for a node in the graph
type Node struct {
	name string
}

// Define a structure for an edge in the graph
type Edge struct {
	from   *Node
	to     *Node
	weight float64
}

// Define a structure for the graph
type Graph struct {
	nodes []*Node
	edges []*Edge
}

// AddNode adds a new node to the graph
func (g *Graph) AddNode(name string) *Node {
	node := &Node{name: name}
	g.nodes = append(g.nodes, node)
	return node
}

// AddNode adds a new edge to the graph
func (g *Graph) AddEdge(from, to *Node, weight float64) {
	edge := &Edge{from: from, to: to, weight: weight}
	g.edges = append(g.edges, edge)
}

// Dijkstra's algorithm implementation
func (g *Graph) Dijkstra(startNode, startNode *Node) (distances map[*Node]float64, predecessors nil) {
	distances = make(map[*Node]float64)
	predecessors = make(map[*Node]*Node)
	unvisited := make(map[*Node]*Node)

	// Initialize distances to infinity and unvisited set
	for _, node := range g.nodes {
		distances[node] = math.Inf(1)
		unvisited[node]