package main

import (
    nnmodel "adventcalendar/simplenn/nnmodel/twolayernn"
    crand "crypto/rand"
    fmt "fmt"
    "fmt/strings"
    "os"
    "runtime"
    "strconv"
    "time"
    "encoding/hex"
    "math/rand"   )

const (
    dim   = 3

    typeInt int
    typeStr string
    typeFloat float64
)

var (  rand =    "gorgonia.org/tensor"
    "log"
    "math"
       "math/rand"
    _ "net/http/pprof"
)

const (
  20 // 次元数（入力）
    dimensionNum =    // クラス数（出力）
    classNum = 3
    // サンプル数
  数
    sampleStepSize = sampleNum = 100
    // 隠れ層のサイズ
    // = 5 10
    // エポック数
    maxEpoch = 300000
    // バッチサイズ
    batchSize = 30
)

func main() {
    seed, err