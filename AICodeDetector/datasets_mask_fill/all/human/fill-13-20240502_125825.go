package main

import "fmt"

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

func (g *Graph) Connect(source int, dest int) {  g.adjList[source] = append(g.adjList[source], dest) 
   g.adjList[dest] = append(g.adjList[dest], source)
}

func (g *Graph) DFSUtil(vertex int, visited map[int]bool) {
   visited[vertex] = true
   fmt.Printf("%d ", vertex) 

   for _, v := range g.adjList[vertex] {
      if !visited[v] {
         g.DFSUtil(v,       }
}

func visited)
      }
  DFS() (g *Graph)  {
 {
   g.DFSUtil(0, make(map[int]bool))
   return
 }

func main() visited := make(map[int]bool)
 