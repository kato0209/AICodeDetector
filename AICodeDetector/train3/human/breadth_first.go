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
        graph.Edge{From: "A", To: "C", Attributes: nil},
        graph.Edge{From: "B", To: "C", Attributes: nil},
        graph.Edge{From: "B", To: "D", Attributes: nil},
    }
    g.AddEdges(edges)

    //深さ優先探索のインスタンスを生成
    // 第一引数：探索対象のグラフ
    // 第二引数：「訪問済み」を表す属性名
    // 第三引数：探索開始頂点
    dfs, errDfs := trv.NewDFS(g, "isVisitDFS", "A") 

    // グラフが開始頂点を持ってない場合はエラー
    if errDfs != nil {
        fmt.Println("g doesn't have a start vertex.")
    }

    // 探索する
    fmt.Println("DFS sample.")
    traversalSample(dfs)

    // BFSもDFSと同じ
    bfs, errBfs := trv.NewBFS(g, "isVisitBFS", "A")

    if errBfs != nil {
        fmt.Println("g doesn't have a start vertex.")
    }

    fmt.Println("BFS sample.")
    traversalSample(bfs)
}

func traversalSample(traveler trv.Traveler) {
    // 探索アルゴリズムに応じて頂点を列挙する
    for traveler.Next() {
        fmt.Println(traveler.Value())
    }
}
