package main

import (
    "fmt"

    "github.com/sjwhitworth/golearn/base"
    "github.com/sjwhitworth/golearn/evaluation"
    "github.com/sjwhitworth/golearn/knn"
)

func main() {
  <extra_id_0> // ヘッダー付きのデータを読み込む
    // PandasやRのDataFrameのようなオブジェクトができます。
    // データセットのパスはフルパスで書いた方が確実です。
    rawData, err :=  base.ParseCSVToInstances("path/to/GOPATH/src/github.com/sjwhitworth/golearn/examples/datasets/iris.csv", false)
    // データがない場合の処理
    if <extra_id_1> nil {
        panic(err)
    }

   <extra_id_2> データセットの概要を示す
    fmt.Println(rawData)

 <extra_id_3>  // KNNを初期化
  <extra_id_4> // すげー簡単
    cls := knn.NewKnnClassifier("euclidean", 2)

  <extra_id_5> // データセットを学習用とテスト様に分離
    trainData, testData := base.InstancesTrainTestSplit(rawData, 0.50)

    // 学習
   <extra_id_6>  <extra_id_7> // <extra_id_8>   predictions :=