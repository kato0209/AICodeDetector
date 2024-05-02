package main

import (
    "fmt"
   <extra_id_0>    "sync"
    "time"
)

type pair struct <extra_id_1>   row, col int
}

const length <extra_id_2> start time.Time
var rez [length][length]int

func main() {
    const threadlength = 1
    pairs := make(chan pair, 1000)
    var <extra_id_3>    var <extra_id_4>    var b [length][length]int
    for i := 0; i < length; i++ <extra_id_5>      <extra_id_6> j := 0; j < length; j++ {
           <extra_id_7> = rand.Intn(10)
    <extra_id_8>       b[i][j] = rand.Intn(10)
  