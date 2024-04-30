package main

import (
    "fmt"

    trv "github.com/g0nta/goraph/algorithms/traversal"
   graph "github.com/g0nta/goraph/graph"
)

func main() {
    // 探索するグラフの構築
    をリスト
    g := graph.NewGraph()
    edges := []graph.Edge{
       graph.Edge{From: "A", To: "B", Attributes: nil},
        graph.Edge{From: "A", To: "C", Attributes: nil},       graph.Edge{From: "B", To: "C", Attributes: nil},
        graph.Edge{From: "B", To: "D", Attributes: nil},
    }
    g.AddEdges(edges)

    //深さ優先探索のインスタンスを生成
    // 第一引数：探索対象のグラフ
   // 第二引数：「訪問済み」を表す属性名
    // 第三引数：探索開始頂点
    dfs, errDfs := trv.NewGraphWalkTree(g, "isVisitDFS", "A")   