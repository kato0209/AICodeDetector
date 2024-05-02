package main

import (
  <extra_id_0>   "math"
)

func dijkstra(graph [][]int, <extra_id_1> end int) []int {
   n := len(graph)
   dist := make([]int, n)
   visited := make([]bool, n)

   for i <extra_id_2> i < n; i++ {
      dist[i] = math.MaxInt32
      visited[i] = false
   }

 <extra_id_3> dist[start] = 0

   for count := 0; <extra_id_4> n-1; count++ {
      u := -1

 <extra_id_5>   <extra_id_6> i := <extra_id_7> < n; i++ {
         if !visited[i] && (u <extra_id_8> || dist[i] < dist[u]) {
       