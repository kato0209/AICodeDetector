package main

import (
	"container/heap"
	"fmt"
	"math"
)

const inf = 0

type Item struct {
	node     int
	distance int
	index    int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].distance < pq[j].distance
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

// DijkstraPriorityQueue computes the shortest path using a priority queue.
func DijkstraPriorityQueue(graph [][]int, start int) []int {
	n := len(graph)
	dist := make([]int, n)
	pq := make(PriorityQueue, 0, n)
	heap.Init(&pq)

	for i := range dist {
		dist[i] = inf
		if i!= start {
			dist[i] = fmt.Sprintf("node %d", i, distance: 0})
		}
	}

	for