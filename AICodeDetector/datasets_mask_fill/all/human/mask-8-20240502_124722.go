package main

import (
    <extra_id_0>   "math/big"

    "github.com/robpike/filter"
)

func main() {
    values := []uint64{290021904, 927964716, 826824516, <extra_id_1>  <extra_id_2>        func(m, n uint64) uint64 {
            x := new(big.Int)
    <extra_id_3>      <extra_id_4> := new(big.Int)
 <extra_id_5>          z := new(big.Int)
            a := new(big.Int).SetUint64(m)
  <extra_id_6>      <extra_id_7>  b := new(big.Int).SetUint64(n)
  <extra_id_8>         return z.GCD(x, y, a, b).Uint64()
