
package main

import (
	"fmt"
	"container/list"
)

type Graph struct {
	vertices int
	adjList  []list.List
}

func NewGraph(v int) *Graph {
	graph := &Graph{
		vertices: v,
		adjList:  make([]list.List, v),
	}
	return graph
}

func (g *Graph) AddEdge(v, w int) {
	g.adjList[v].PushBack(w)
}

func (g *Graph) BFS(s int) {
	visited := make([]bool, g.vertices)
	queue := list.New()
	visited[s] = true
	queue.PushBack(s)

	for queue.Len() > 0 {
		s := queue.Remove(queue.Front()).(int)
		fmt.Printf("%d ", s)

		for e := g.adjList[s].Front(); e != nil; e = e.Next() {
			if !visited[e.Value.(int)] {
				visited[e.Value.(int)] = true
				queue.PushBack(e.Value.(int))
			}
		}
	}
}

func main() {
	// Create a graph given the above diagram
	g := NewGraph(4)
	g.AddEdge(0, 1)
	g.AddEdge(0, 2)
	g.AddEdge(1, 2)
	g.AddEdge(2, 0)
	g.AddEdge(2, 3)
	g.AddEdge(3, 3)

	fmt.Println("Following is Breadth First Traversal (starting from vertex 2)")
	g.BFS(2)
}
