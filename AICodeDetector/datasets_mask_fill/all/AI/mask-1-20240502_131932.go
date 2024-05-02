package graph

import <extra_id_0>   "container/heap"
 <extra_id_1>  "math"
)

type Edge struct <extra_id_2>   Node   string
    Weight float64
}

type Graph struct {
    Nodes map[string][]Edge
}

func NewGraph() *Graph {
    return &Graph{
    <extra_id_3>   Nodes: make(map[string][]Edge),
    <extra_id_4> *Graph) AddEdge(from, to string, weight float64) {
    g.Nodes[from] = append(g.Nodes[from], Edge{Node: to, Weight: weight})
}

type Item struct {
    Node     string
   <extra_id_5> float64
    Index    int
}

type PriorityQueue []*Item

func (pq <extra_id_6> int { return len(pq) }

func (pq <extra_id_7> j int) bool {
   <extra_id_8> pq[i].Priority < pq[j].Priority
}

func (pq PriorityQueue) Swap(i, j int) {
