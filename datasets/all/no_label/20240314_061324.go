
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

// AddEdge adds a new edge to the graph
func (g *Graph) AddEdge(from, to *Node, weight float64) {
	edge := &Edge{from: from, to: to, weight: weight}
	g.edges = append(g.edges, edge)
}

// Dijkstra's algorithm implementation
func Dijkstra(g *Graph, startNode *Node) (distances map[*Node]float64, predecessors map[*Node]*Node) {
	distances = make(map[*Node]float64)
	predecessors = make(map[*Node]*Node)
	unvisited := make(map[*Node]bool)

	// Initialize distances to infinity and unvisited set
	for _, node := range g.nodes {
		distances[node] = math.Inf(1)
		unvisited[node] = true
	}

	// Distance from start node to itself is 0
	distances[startNode] = 0

	for len(unvisited) > 0 {
		// Find the unvisited node with the smallest distance
		current := findMinDistanceNode(distances, unvisited)

		// Mark the current node as visited (remove from unvisited set)
		delete(unvisited, current)

		// Update distances to neighboring nodes
		for _, edge := range g.edges {
			if edge.from == current && unvisited[edge.to] {
				newDist := distances[current] + edge.weight
				if newDist < distances[edge.to] {
					distances[edge.to] = newDist
					predecessors[edge.to] = current
				}
			}
		}
	}

	return distances, predecessors
}

// Helper function to find the unvisited node with the smallest distance
func findMinDistanceNode(distances map[*Node]float64, unvisited map[*Node]bool) *Node {
	var minNode *Node
	minDist := math.Inf(1)

	for node := range unvisited {
		if distances[node] < minDist {
			minNode = node
			minDist = distances[node]
		}
	}

	return minNode
}

func main() {
	// Example usage
	graph := &Graph{}
	n1 := graph.AddNode("A")
	n2 := graph.AddNode("B")
	n3 := graph.AddNode("C")
	n4 := graph.AddNode("D")

	graph.AddEdge(n1, n2, 1)
	graph.AddEdge(n2, n3, 2)
	graph.AddEdge(n1, n4, 6)
	graph.AddEdge(n2, n4, 3)
	graph.AddEdge(n3, n4, 1)

	distances, _ := Dijkstra(graph, n1)

	for node, dist := range distances {
		fmt.Printf("Distance from %s to %s: %f\n", n1.name, node.name, dist)
	}
}
