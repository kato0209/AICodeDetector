package graph

import (
    "container/heap"
    "math"
)

type Edge struct {
    Node   string
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
    Priority float64
    Index    int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
    return pq[i].Priority < pq[j].Priority
}

func (pq PriorityQueue) Swap(i, j int) {
    pq[i], pq[j] = pq[j], pq[i]
    pq[i].Index = i
    pq[j].Index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
    n := len(*pq)
    item := x.(*Item)
    item.Index = n
    *pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    item := old[n-1]
    old[n-1] = nil
    item.Index = -1
    *pq = old[0 : n-1]
    return item
}

func (g *Graph) Dijkstra(start, target string) float64 {
    dist := make(map[string]float64)
    for node := range g.Nodes {
        dist[node] = math.Inf(1)
    }
    dist[start] = 0

    pq := make(PriorityQueue, 0)
    heap.Push(&pq, &Item{
        Node:     start,
        Priority: 0,
    })

    for pq.Len() > 0 {
        item := heap.Pop(&pq).(*Item)
        node := item.Node

        if node == target {
            return dist[node]
        }

        for _, edge := range g.Nodes[node] {
            next := edge.Node
            newDist := dist[node] + edge.Weight
            if newDist < dist[next] {
                dist[next] = newDist
                heap.Push(&pq, &Item{
                    Node:     next,
                    Priority: newDist,
                })
            }
        }
    }
    return math.Inf(1)
}

// Example usage:
// g := NewGraph()
// g.AddEdge("A", "B", 1.0)
// g.AddEdge("B",
