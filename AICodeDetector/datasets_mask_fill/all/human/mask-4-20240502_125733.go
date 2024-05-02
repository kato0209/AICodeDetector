package <extra_id_0>    "fmt"

    "github.com/sjwhitworth/golearn/base"
    <extra_id_1>   "github.com/sjwhitworth/golearn/knn"
)

func main() {
    // ヘッダー付きのデータを読み込む
    // PandasやRのDataFrameのようなオブジェクトができます。
    // データセットのパスはフルパスで書いた方が確実です。
    rawData, err :=  base.ParseCSVToInstances("path/to/GOPATH/src/github.com/sjwhitworth/golearn/examples/datasets/iris.csv", false)
    // <extra_id_2>   if err != nil {
 <extra_id_3>   <extra_id_4>  panic(err)
    }

    // データセットの概要を示す
    fmt.Println(rawData)

    // KNNを初期化
    // すげー簡単
    cls := knn.NewKnnClassifier("euclidean", 2)

    // データセットを学習用とテスト様に分離
  <extra_id_5> trainData, testData := base.InstancesTrainTestSplit(rawData, <extra_id_6>  <extra_id_7> 学習
    <extra_id_8>   // テストデータを使って予測
    predictions :=