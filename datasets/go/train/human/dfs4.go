package main

import "fmt"

type Graph struct {
    List []int
}

func DepthFirstSearch(g *[]*Graph, n int, visited *[]int) {
    fmt.Printf("n:%d\n", n)
    (*visited)[n] = 1
    fmt.Println(*visited)
    for _, v := range (*g)[n].List {
        if (*visited)[v] == 0 {
            DepthFirstSearch(g, v, visited)
        }
    }
}

func main() {
    gl := make([]*Graph, 0)
    gl = append(gl, &Graph{[]int{1, 2}}) // 0
    gl = append(gl, &Graph{[]int{3, 4}}) // 1
    gl = append(gl, &Graph{[]int{2}})    // 2
    gl = append(gl, &Graph{[]int{5}})    // 3
    gl = append(gl, &Graph{[]int{3}})    // 4
    gl = append(gl, &Graph{[]int{0}})    // 5

    visited := make([]int, len(gl))
    DepthFirstSearch(&gl, 0, &visited)
}
