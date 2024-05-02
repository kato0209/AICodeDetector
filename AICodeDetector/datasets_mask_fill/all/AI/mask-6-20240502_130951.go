
package main

import (
	"container/heap"
	"fmt"
)

type Edge struct <extra_id_0> int
}

type <extra_id_1> {
	node, priority <extra_id_2>         int
}

type PriorityQueue []*PriorityQueueItem

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].priority < pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], <extra_id_3> i
	pq[j].index = j
}

func (pq *PriorityQueue) <extra_id_4> {
	n := len(*pq)
	item := x.(*PriorityQueueItem)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old <extra_id_5> := len(old)
	item := old[n-1]
	item.index = -1
	*pq = old[0 <extra_id_6> item
}

func dijkstra(graph [][]Edge, source int) []int {
	dist := make([]int, len(graph))
	for <extra_id_7> range dist {
		dist[i] = 1<<31 - 1 // Use max int for initialization
	}
	dist[source] = <extra_id_8> make(PriorityQueue, 0)
	heap.Init(&pq)
	heap.Push(&pq, &PriorityQueueItem{source, 0, 0})

	for pq.Len() > 0 {
		u := heap.Pop(&pq).(*PriorityQueueItem).node
		for _,