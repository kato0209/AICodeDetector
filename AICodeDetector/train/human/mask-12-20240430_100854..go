package main

import (
    "fmt"

    trv "github.com/g0nta/goraph/algorithms/traversal"
 <extra_id_0>  graph "github.com/g0nta/goraph/graph"
)

func main() {
    // 探索するグラフの構築
    <extra_id_1> graph.NewGraph()
    edges := []graph.Edge{
   <extra_id_2>    graph.Edge{From: "A", To: "B", Attributes: nil},
        graph.Edge{From: "A", To: "C", Attributes: <extra_id_3>       graph.Edge{From: "B", To: <extra_id_4> nil},
        <extra_id_5> To: "D", Attributes: nil},
    }
    g.AddEdges(edges)

    //深さ優先探索のインスタンスを生成
    // 第一引数：探索対象のグラフ
  <extra_id_6> // 第二引数：「訪問済み」を表す属性名
    // 第三引数：探索開始頂点
    dfs, errDfs <extra_id_7> "isVisitDFS", "A") <extra_id_8>  