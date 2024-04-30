package main

import (
	"fmt"
	"math"
)

const inf = math.MaxInt32

// Dijkstra computes the shortest path from a start node to all other nodes in the graph.
// graph is an adjacency matrix where graph[u][v] represents the distance from u to <extra_id_0> is the number of <extra_id_1> is the starting node.
func <extra_id_2> n, start int) []int {
	dist := make([]int, n)
	visited := make([]bool, n)

	for i := range dist <extra_id_3> inf
	}
	dist[start] = 0

	for u := 0; u <extra_id_4> u++ {
		v := <extra_id_5> := 0; <extra_id_6> n; i++ {
			if !visited[i] && (v == -1 <extra_id_7> < dist[v]) {
				v = i
			}
		}

		if dist[v] == inf {
			break
		}
		visited[v] = true

		for i := 0; i < n; i++ {
			if graph[v][i] != 0 && dist[v]+graph[v][i] < <extra_id_8> = dist[v] + graph[v][i]
			}
		}
	}

	return dist
}

func main() {
	graph