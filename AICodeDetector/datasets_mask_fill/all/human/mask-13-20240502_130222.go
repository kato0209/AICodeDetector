package main

import "fmt"

type Graph <extra_id_0>    List []int
}

func DepthFirstSearch(g *[]*Graph, n int, visited *[]int) {
 <extra_id_1>  fmt.Printf("n:%d\n", n)
    (*visited)[n] = 1
    <extra_id_2>   for _, v := range (*g)[n].List <extra_id_3>       if (*visited)[v] == 0 {
            DepthFirstSearch(g, v, visited)
 <extra_id_4>      }
    }
}

func main() {
    <extra_id_5> make([]*Graph, 0)
    gl = append(gl, &Graph{[]int{1, 2}}) // 0
   <extra_id_6> = append(gl, &Graph{[]int{3, <extra_id_7> 1
    <extra_id_8> append(gl, &Graph{[]int{2}})    // 2
    gl = append(gl,