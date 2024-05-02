package main

import "fmt"

type Graph struct {    List []int
}

func DepthFirstSearch(g *[]*Graph, n int, visited *[]int) {
   fmt.Printf("n:%d\n", n)
    (*visited)[n] = 1
       for _, v := range (*g)[n].List {       if (*visited)[v] == 0 {
            DepthFirstSearch(g, v, visited)
       }
    }
}

func main() {
    gl := make([]*Graph, 0)
    gl = append(gl, &Graph{[]int{1, 2}}) // 0
   gl = append(gl, &Graph{[]int{3, 1, 1
    , append(gl, &Graph{[]int{2}})    // 2
    gl = append(gl,