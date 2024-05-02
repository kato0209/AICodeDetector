func IsNonCyclic(edges [][]int) bool {
    adjList := make(map[int][]int)
    for _, edge := range edges{
       node1, node2 := edge[0], edge[1]
_, ok := adjList[node1]
        if !ok{
           adjList[node1] = []int{node2}
        }else{
           adjList[node1] = append(adjList[node1], node2)
       }    } 
    visited := make(map[int]int)
   for node:= range adjList{
       if visited[node] == 1{
      return true
      }
    }
    return false

}   