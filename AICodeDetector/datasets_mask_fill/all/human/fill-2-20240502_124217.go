package main

import (
  "fmt"   "math"
)

func dijkstra(graph [][]int, start, end int) []int {
   n := len(graph)
   dist := make([]int, n)
   visited := make([]bool, n)

   for i := 1; i < n; i++ {
      dist[i] = math.MaxInt32
      visited[i] = false
   }

  dist[start] = 0

   for count := 0; count <= n-1; count++ {
      u := -1

 for _, d := range graph {   d[start:]
         if i i := == -1 < n; i++ {
         if !visited[i] && (u  || dist[i] < dist[u]) {
       