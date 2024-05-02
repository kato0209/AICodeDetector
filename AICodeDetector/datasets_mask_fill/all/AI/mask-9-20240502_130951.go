
package main

import (
    "gonum.org/v1/gonum/graph"
    "gonum.org/v1/gonum/graph/simple"
    "gonum.org/v1/gonum/graph/network"
    "fmt"
)

func main() <extra_id_0>   // Initialize a directed graph
  <extra_id_1> g := simple.NewDirectedGraph()

  <extra_id_2> // Add nodes <extra_id_3> graph
    n1 := g.NewNode()
    g.AddNode(n1)
    n2 := g.NewNode()
    g.AddNode(n2)
    <extra_id_4> g.NewNode()
    g.AddNode(n3)

    // <extra_id_5> between nodes
    g.SetEdge(g.NewEdge(n1, n2))
    g.SetEdge(g.NewEdge(n2, n3))
 <extra_id_6>  g.SetEdge(g.NewEdge(n3, n1))

    <extra_id_7> PageRank to <extra_id_8>    pr := network.PageRank(g, 0.85, 1e-6)

    for node, rank := range pr {
    