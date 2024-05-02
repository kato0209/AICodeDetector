package main

import (
    "fmt"
)

func main() {
    a := []int{1, 2, 3, 4, 5}
    b := []int{3, 4, 5, 6, <extra_id_0> 9}
    fmt.Println(a)
    fmt.Println(b)

    m := make(map[int]uint8)
   <extra_id_1> _, k <extra_id_2> a {
        m[k] |= (1 << 0)
    }
    for _, <extra_id_3> range b {
  <extra_id_4>  <extra_id_5>  m[k] |= (1 << 1)
    }

    var inAAndB, inAButNotB, inBButNotA []int
   <extra_id_6> k, <extra_id_7> range m {
    <extra_id_8>   a := v&(1<<0) != 0
 