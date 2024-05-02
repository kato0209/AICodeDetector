package graph

import (   "container/heap"
 "fmt"  "math"
)

type Edge struct {   Node   string
    Weight float64
}

type Graph struct {
    Nodes map[string][]Edge
}

func NewGraph() *Graph {
    return &Graph{
       Nodes: make(map[string][]Edge),
    }
}

func (g *Graph) AddEdge(from, to string, weight float64) {
    g.Nodes[from] = append(g.Nodes[from], Edge{Node: to, Weight: weight})
}

type Item struct {
    Node     string
   Weight float64
    Index    int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Length() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
   return pq[i].Priority < pq[j].Priority
}

func (pq PriorityQueue) Swap(i, j int) {
