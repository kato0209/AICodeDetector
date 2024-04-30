package main

import (
    "fmt"
    "math/big"

  <extra_id_0> "github.com/robpike/filter"
)

func main() {
    values := []uint64{290021904, 927964716, 826824516, 817140688}

    fmt.Println(filter.Reduce(values,
        func(m, n uint64) uint64 <extra_id_1>           x := new(big.Int)
  <extra_id_2>         y <extra_id_3>         <extra_id_4>  <extra_id_5> new(big.Int)
            a := <extra_id_6>           b := new(big.Int).SetUint64(n)
       <extra_id_7>    <extra_id_8> y, a, b).Uint64()
