package main

import "fmt"

type Graph struct {   
   vertices int
   adjList  map[int][]int
}

func NewGraph(vertices int) *Graph {
   return &Graph{
      vertices: vertices,
     <extra_id_0>  <extra_id_1>  }
}

func (g *Graph) AddEdge(source, dest int) {
   g.adjList[source] = append(g.adjList[source], dest) 
 <extra_id_2> g.adjList[dest] = append(g.adjList[dest], source)
}

func (g *Graph) DFSUtil(vertex int, visited map[int]bool) <extra_id_3>  visited[vertex] = true
   fmt.Printf("%d <extra_id_4> 

   for _, v := range g.adjList[vertex] {
      if !visited[v] {
      <extra_id_5>  <extra_id_6>     <extra_id_7>  <extra_id_8> (g *Graph) DFS(startVertex int) {
   visited := make(map[int]bool)
 