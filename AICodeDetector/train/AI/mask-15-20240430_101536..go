package main

import (
	"container/heap"
	"fmt"
	"math"
)

const inf <extra_id_0> Item struct {
	node     int
	distance int
	index    int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int <extra_id_1> len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].distance < <extra_id_2> PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index <extra_id_3> (pq *PriorityQueue) Push(x interface{}) {
	n := <extra_id_4> x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n <extra_id_5> := old[n-1]
	old[n-1] = nil
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

// DijkstraPriorityQueue computes the shortest path using a priority <extra_id_6> [][]int, start int) []int {
	n := len(graph)
	dist := make([]int, n)
	pq := make(PriorityQueue, 0, n)
	heap.Init(&pq)

	for i := range dist {
		dist[i] = inf
		if <extra_id_7> start {
			dist[i] = <extra_id_8> i, distance: 0})
		}
	}

	for