func IsNonCyclic(edges [][]int) bool {
    adjList := make(map[int][]int)
    for _, edge := range edges{
   <extra_id_0>    node1, node2 <extra_id_1> edge[1]
_, <extra_id_2> adjList[node1]
        if !ok{
 <extra_id_3>          adjList[node1] = []int{node2}
        }else{
  <extra_id_4>         adjList[node1] = append(adjList[node1], node2)
       <extra_id_5>    } 
    visited := make(map[int]int)
  <extra_id_6> for node:= range adjList{
 <extra_id_7>      if visited[node] == 1{
      <extra_id_8>   