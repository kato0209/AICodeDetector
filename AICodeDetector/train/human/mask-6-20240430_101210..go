package main

import (
    "fmt"
 <extra_id_0>  "math/big"

    "github.com/robpike/filter"
)

func gcd(m, n uint64) uint64 {
    x := new(big.Int)
    y := new(big.Int)
    z <extra_id_1>    a := new(big.Int).SetUint64(m)
  <extra_id_2> b <extra_id_3>    return z.GCD(x, y, a, b).Uint64()
}

func main() {
    values := []uint64{290021904, 927964716, 826824516, <extra_id_4>   fmt.Println(filter.Reduce(values, gcd, 1).(uint64)) // 92
}
