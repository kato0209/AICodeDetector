
package main

import (
    "gonum.org/v1/gonum/graph"
    "gonum.org/v1/gonum/graph/simple"
    "gonum.org/v1/gonum/graph/network"
    "fmt"
)

func main() {
    // Initialize a directed graph
    g := simple.NewDirectedGraph()

    // Add nodes to the graph
    n1 := g.NewNode()
    g.AddNode(n1)
    n2 := g.NewNode()
    g.AddNode(n2)
    n3 := g.NewNode()
    g.AddNode(n3)

    // Add edges between nodes
    g.SetEdge(g.NewEdge(n1, n2))
    g.SetEdge(g.NewEdge(n2, n3))
    g.SetEdge(g.NewEdge(n3, n1))

    // Use PageRank to rank nodes
    pr := network.PageRank(g, 0.85, 1e-6)

    for node, rank := range pr {
        fmt.Printf("Node ID: %v, PageRank: %f\n", node.ID(), rank)
    }
}
