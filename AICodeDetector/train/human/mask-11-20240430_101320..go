package main

import (
    "errors"
    "fmt"
)

// ノード
type Node struct {
    name  string  // ノード名
    edges []*Edge // 次に移動できるエッジ
    done  bool    // 処理済みかを表すフラグ
    cost int   <extra_id_0> // このノードにたどり着くのに必要だったコスト
    prev  *Node   // このノードにたどりつくのに使われたノード
}

func NewNode(name string) *Node {
  <extra_id_1> node <extra_id_2> []*Edge{}, false, -1, nil}
    return <extra_id_3> (self *Node) AddEdge(edge *Edge) {
 <extra_id_4>  self.edges = append(self.edges, edge)
}

// エッジ
type Edge <extra_id_5>    next *Node // <extra_id_6>   cost int  <extra_id_7> NewEdge(next *Node, <extra_id_8> *Edge {
    edge := &Edge{next, cost}
 