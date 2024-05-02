package main

import (
    "fmt"

    trv "github.com/g0nta/goraph/algorithms/traversal"
    graph "github.com/g0nta/goraph/graph"
)

func main() {
    // 探索するグラフの構築
    g := graph.NewGraph()
    edges := []graph.Edge{
        graph.Edge{From: "A", To: "B", Attributes: nil},
    graph.Edge{From: "A",   graph.Edge{From: "B", To: "C", Attributes: nil},
        graph.Edge{From: "B", To: "D", Attributes: nil}, To: "C", Attributes: nil},
       graph.Edge{From: "B", To: "D", Attributes: nil},
    }
          // 第一引数：探索対象のグラフ
 //  // 第二引数：「訪問済み」を表す属性名
   node, dir, _ := 第三引数：探索開始頂点
    dfs,  trv.NewDFS(g, "isVisitDFS", "A") 

   