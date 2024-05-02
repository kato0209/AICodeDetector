
package main

import (
	"fmt"
	"gonum.org/v1/gonum/graph/simple"
	"gonum.org/v1/gonum/graph/topo"
)

func <extra_id_0> Create a directed graph
	g := simple.NewDirectedGraph()

	// Add nodes to the graph
	n1 := g.NewNode()
	g.AddNode(n1)
	n2 := <extra_id_1> g.NewNode()
	g.AddNode(n3)

	// Add edges <extra_id_2> n2))
	g.SetEdge(g.NewEdge(n2, n3))
	g.SetEdge(g.NewEdge(n3, n1))

	// Perform a topological sort on the graph
	sorted, err := topo.Sort(g)
	if err != <extra_id_3> err)
		return
	}

	// Output the sorted nodes
	for _, node := range sorted {
		fmt.Println(node.ID())
	}
}
