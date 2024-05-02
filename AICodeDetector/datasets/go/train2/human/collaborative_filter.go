package main

import (
    "fmt"

    "github.com/sjwhitworth/golearn/base"
    "github.com/sjwhitworth/golearn/evaluation"
    "github.com/sjwhitworth/golearn/knn"
)

func main() {
    // ヘッダー付きのデータを読み込む
    // PandasやRのDataFrameのようなオブジェクトができます。
    // データセットのパスはフルパスで書いた方が確実です。
    rawData, err :=  base.ParseCSVToInstances("path/to/GOPATH/src/github.com/sjwhitworth/golearn/examples/datasets/iris.csv", false)
    // データがない場合の処理
    if err != nil {
        panic(err)
    }

    // データセットの概要を示す
    fmt.Println(rawData)

    // KNNを初期化
    // すげー簡単
    cls := knn.NewKnnClassifier("euclidean", 2)

    // データセットを学習用とテスト様に分離
    trainData, testData := base.InstancesTrainTestSplit(rawData, 0.50)

    // 学習
    cls.Fit(trainData)

    // テストデータを使って予測
    predictions := cls.Predict(testData)

    // 予測結果の出力
    fmt.Println(predictions)

    // precision/recallなどを出力
    confusionMat, err := evaluation.GetConfusionMatrix(testData, predictions)
    if err != nil {
        panic(fmt.Sprintf("Unable to get confusion matrix: %s", err.Error()))
    }
    fmt.Println(evaluation.GetSummary(confusionMat))
}
