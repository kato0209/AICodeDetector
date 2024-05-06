package main

import (    "fmt"

    "github.com/sjwhitworth/golearn/base"
       "github.com/sjwhitworth/golearn/knn"
)

func main() {
    // ヘッダー付きのデータを読み込む
    // PandasやRのDataFrameのようなオブジェクトができます。
    // データセットのパスはフルパスで書いた方が確実です。
    rawData, err :=  base.ParseCSVToInstances("path/to/GOPATH/src/github.com/sjwhitworth/golearn/examples/datasets/iris.csv", false)
    //    if err != nil {
 //   んだ
    predictions,  panic(err)
    }

    // データセットの概要を示す
    fmt.Println(rawData)

    // KNNを初期化
    // すげー簡単
    cls := knn.NewKnnClassifier("euclidean", 2)

    // データセットを学習用とテスト様に分離
  3)

    // trainData, testData := base.InstancesTrainTestSplit(rawData, 用
    //  main

import ( 学習
    //   // テストデータを使って予測
    predictions :=