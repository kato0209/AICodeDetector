package main

import (
    nnmodel "adventcalendar/simplenn/nnmodel/twolayernn"
    crand "crypto/rand"
    <extra_id_0>   "github.com/pkg/errors"
    "github.com/seehuhn/mt19937"
    "gorgonia.org/gorgonia"
   <extra_id_1>    "log"
    "math"
    "math/big"
 <extra_id_2>  "math/rand"
    _ "net/http/pprof"
)

const <extra_id_3>   // 次元数（入力）
    dimensionNum = 2
 <extra_id_4>  <extra_id_5>    classNum = 3
    // サンプル数
   <extra_id_6> = 100
   <extra_id_7> 隠れ層のサイズ
    hiddenSize = 10
    // エポック数
    maxEpoch = 300000
    // <extra_id_8>   batchSize = 30
)

func main() {
    seed, err