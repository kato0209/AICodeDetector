
package main

import (
	"fmt"
	"math"
)

// Define a structure for the result
type Result struct {
	Distance map[string]int
	Path     map[string]string
}

// Dijkstra algorithm implementation
func Dijkstra(graph map[string]map[string]int, start string) Result {
	dist := make(map[string]int)
	prev := make(map[string]string)

	// Initialize distances to infinity and previous nodes to none
	for vertex := range graph {
		dist[vertex] = math.MaxInt32
		prev[vertex] = ""
	}
	dist[start] = 0

	unvisited := make(map[string]bool)
	for vertex := range graph {
		unvisited[vertex] = true
	}

	for len(unvisited) != 0 {
		// Find the unvisited vertex with the smallest distance
		u := ""
		smallestDist := math.MaxInt32
		for vertex := range unvisited {
			if dist[vertex] < smallestDist {
				smallestDist = dist[vertex]
				u = vertex
			}
		}

		delete(unvisited, u)

		// Update distances for neighbors of the current vertex
		for neighbor, weight := range graph[u] {
			alt := dist[u] + weight
			if alt < dist[neighbor] {
				dist[neighbor] = alt
				prev[neighbor] = u
			}
		}
	}

	return Result{Distance: dist, Path: prev}
}

func main() {
	graph := map[string]map[string]int{
		"A": {"B": 1, "C": 4},
		"B": {"A": 1, "C": 2, "D": 5},
		"C": {"A": 4, "B": 2, "D": 1},
		"D": {"B": 5, "C": 1},
	}

	result := Dijkstra(graph, "A")
	fmt.Println("Distances:", result.Distance)
	fmt.Println("Paths:", result.Path)
}
