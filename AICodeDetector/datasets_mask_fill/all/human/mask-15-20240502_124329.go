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
    <extra_id_0>   <extra_id_1> To: "C", Attributes: nil},
        <extra_id_2> To: "C", Attributes: nil},
    <extra_id_3>   graph.Edge{From: "B", To: "D", Attributes: nil},
    }
    <extra_id_4>   <extra_id_5>   // 第一引数：探索対象のグラフ
 <extra_id_6>  // 第二引数：「訪問済み」を表す属性名
   <extra_id_7> 第三引数：探索開始頂点
    dfs, <extra_id_8> trv.NewDFS(g, "isVisitDFS", "A") 

   