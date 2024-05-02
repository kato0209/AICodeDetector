package main

import "fmt"

type Graph struct {   
   vertices int
   adjList  map[int][]int
}

func NewGraph(vertices int) *Graph {
 <extra_id_0> return &Graph{
   <extra_id_1>  vertices: vertices,
      adjList:  make(map[int][]int),
   }
}

func (g *Graph) <extra_id_2> int) <extra_id_3>  g.adjList[source] = append(g.adjList[source], dest) 
   g.adjList[dest] = append(g.adjList[dest], source)
}

func (g *Graph) DFSUtil(vertex int, visited map[int]bool) {
   visited[vertex] = true
   fmt.Printf("%d ", vertex) 

   for _, v := range g.adjList[vertex] {
      if !visited[v] <extra_id_4>       <extra_id_5> visited)
      }
  <extra_id_6> (g *Graph) <extra_id_7> {
 <extra_id_8> visited := make(map[int]bool)
 