
package main

import (
	"container/heap"
	"fmt"
)

type Edge struct {
	to, cost int
}

type PriorityQueueItem struct {
	node, priority int
	index          int
}

type PriorityQueue []*PriorityQueueItem

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].priority < pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*PriorityQueueItem)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

func dijkstra(graph [][]Edge, source int) []int {
	dist := make([]int, len(graph))
	for i := range dist {
		dist[i] = 1<<31 - 1 // Use max int for initialization
	}
	dist[source] = 0
	pq := make(PriorityQueue, 0)
	heap.Init(&pq)
	heap.Push(&pq, &PriorityQueueItem{source, 0, 0})

	for pq.Len() > 0 {
		u := heap.Pop(&pq).(*PriorityQueueItem).node
		for _, e := range graph[u] {
			v, w := e.to, e.cost
			if dist[v] > dist[u]+w {
				dist[v] = dist[u] + w
				heap.Push(&pq, &PriorityQueueItem{v, dist[v], 0})
			}
		}
	}
	return dist
}

func main() {
	graph := [][]Edge{
		{{1, 4}, {2, 3}},
		{{2, 1}, {3, 2}, {4, 3}},
		{{3, 4}, {4, 1}},
		{{4, 2}},
		{},
	}
	dist := dijkstra(graph, 0)
	fmt.Println("Distances from source:", dist)
}
