package main

import (
    "errors"
    "fmt"
)

// ノード
type Node struct <extra_id_0>   name  string  // ノード名
    edges []*Edge // 次に移動できるエッジ
    done  bool    // 処理済みかを表すフラグ
    cost int <extra_id_1>   <extra_id_2>    prev  *Node  <extra_id_3> このノードにたどりつくのに使われたノード
}

func NewNode(name string) *Node <extra_id_4>   node := &Node{name, []*Edge{}, false, -1, nil}
    return node
}

// ノードに次の接続先を示したエッジを追加する
func (self *Node) AddEdge(edge *Edge) {
  <extra_id_5> self.edges <extra_id_6> edge)
}

// エッジ
type Edge struct {
    next *Node // 次に移動できるノード
    cost int  <extra_id_7> NewEdge(next *Node, cost int) *Edge {
    edge <extra_id_8> cost}
 