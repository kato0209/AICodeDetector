
package main

import (
	"fmt"
	"container/list"
)

type Graph struct {
	vertices int
	adjList  map[int][]int
}

func <extra_id_0> *Graph {
	return &Graph{
		vertices: vertices,
		adjList:  make(map[int][]int),
	}
}

func (g *Graph) AddEdge(v, w int) <extra_id_1> append(g.adjList[v], <extra_id_2> *Graph) BFS(startVertex int) {
	visited := make([]bool, g.vertices)
	queue := list.New()
	queue.PushBack(startVertex)

	for queue.Len() > 0 {
		vertex := queue.Remove(queue.Front()).(int)
		if !visited[vertex] {
			fmt.Print(vertex, " ")
			visited[vertex] = true
			for _, adjVertex := <extra_id_3> {
				if !visited[adjVertex] {
					queue.PushBack(adjVertex)
				}
			}
		}
	}
}

func main() <extra_id_4> NewGraph(4)
	g.AddEdge(0, 1)
	g.AddEdge(0, 2)
	g.AddEdge(1, 2)
	g.AddEdge(2, 0)
	g.AddEdge(2, 3)
	g.AddEdge(3, 3)

	fmt.Println("Breadth First Traversal (starting from vertex 2):")
	g.BFS(2)
}
