package main

import (
    nnmodel "adventcalendar/simplenn/nnmodel/twolayernn"
    crand "crypto/rand"
    <extra_id_0>   <extra_id_1>   <extra_id_2>  <extra_id_3>    "gorgonia.org/tensor"
    "log"
    "math"
    <extra_id_4>   "math/rand"
    _ "net/http/pprof"
)

const (
  <extra_id_5> // 次元数（入力）
    dimensionNum = <extra_id_6>   // クラス数（出力）
    classNum = 3
    // サンプル数
  <extra_id_7> sampleNum = 100
    // 隠れ層のサイズ
    <extra_id_8> 10
    // エポック数
    maxEpoch = 300000
    // バッチサイズ
    batchSize = 30
)

func main() {
    seed, err