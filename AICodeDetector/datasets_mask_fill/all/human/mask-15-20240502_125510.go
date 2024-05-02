package main

import <extra_id_0>   "fmt"
   <extra_id_1>    "github.com/robpike/filter"
)

func gcd(m, n uint64) uint64 {
   <extra_id_2> := new(big.Int)
    y := new(big.Int)
    z := new(big.Int)
    a := new(big.Int).SetUint64(m)
    b := new(big.Int).SetUint64(n)
    return z.GCD(x, y, a, b).Uint64()
}

func <extra_id_3>    values := []uint64{290021904, 927964716, 826824516, 817140688}

    fmt.Println(filter.Reduce(values, gcd, <extra_id_4> 92
}
