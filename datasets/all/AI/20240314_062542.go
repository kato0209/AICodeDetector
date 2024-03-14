
package main

import (
	"fmt"
	"container/list"
)

type Graph struct {
	vertices int
	adjList  map[int][]int
}

func NewGraph(vertices int) *Graph {
	return &Graph{
		vertices: vertices,
		adjList:  make(map[int][]int),
	}
}

func (g *Graph) AddEdge(v, w int) {
	g.adjList[v] = append(g.adjList[v], w)
}

func (g *Graph) BFS(startVertex int) {
	visited := make([]bool, g.vertices)
	queue := list.New()
	queue.PushBack(startVertex)

	for queue.Len() > 0 {
		vertex := queue.Remove(queue.Front()).(int)
		if !visited[vertex] {
			fmt.Print(vertex, " ")
			visited[vertex] = true
			for _, adjVertex := range g.adjList[vertex] {
				if !visited[adjVertex] {
					queue.PushBack(adjVertex)
				}
			}
		}
	}
}

func main() {
	g := NewGraph(4)
	g.AddEdge(0, 1)
	g.AddEdge(0, 2)
	g.AddEdge(1, 2)
	g.AddEdge(2, 0)
	g.AddEdge(2, 3)
	g.AddEdge(3, 3)

	fmt.Println("Breadth First Traversal (starting from vertex 2):")
	g.BFS(2)
}
