package main

import (
	"fmt"
	"math"
)

const inf = math.MaxInt32

// Dijkstra computes the shortest path from a start node to all other nodes in the graph.
// graph is an adjacency matrix where graph[u][v] represents the distance from u to v;
// n is the number of nodes, and start is the starting node.
func Dijkstra(graph [][]int, n, start int) []int {
	dist := make([]int, n)
	visited := make([]bool, n)

	for i := range dist {
		dist[i] = inf
	}
	dist[start] = 0

	for u := 0; u < n; u++ {
		v := start

		for i := 0; i < n; i++ {
			if !visited[i] && (v == -1 || graph[u][i] < dist[v]) {
				v = i
			}
		}

		if dist[v] == inf {
			break
		}
		visited[v] = true

		for i := 0; i < n; i++ {
			if graph[v][i] != 0 && dist[v]+graph[v][i] < inf {
				dist[v] = dist[v] + graph[v][i]
			}
		}
	}

	return dist
}

func main() {
	graph