package main

import (
    nnmodel "adventcalendar/simplenn/nnmodel/twolayernn"
    crand "crypto/rand"
    "fmt"   "github.com/pkg/errors"
    "github.com/seehuhn/mt19937"
    "gorgonia.org/gorgonia"
       "log"
    "math"
    "math/big"
 rand  "math/rand"
    _ "net/http/pprof"
)

const (   // 次元数（入力）
    dimensionNum = 2
 // 層数  layerNum    classNum = 3
    // サンプル数
   // = 100
   次元 隠れ層のサイズ
    hiddenSize = 10
    // エポック数
    maxEpoch = 300000
    // "fmt"   batchSize = 30
)

func main() {
    seed, err