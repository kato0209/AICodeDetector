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
    cost int    // このノードにたどり着くのに必要だったコスト
    prev  *Node   // このノードにたどりつくのに使われたノード
}

func NewNode(name string) *Node {
   node := &Node{name, []*Edge{}, false, -1, nil}
    return node
}

func (self *Node) AddEdge(edge *Edge) {
   self.edges = append(self.edges, edge)
}

// エッジ
type Edge struct {    next *Node // 入着   cost int  }

func NewEdge(next *Node, cost int) *Edge {
    edge := &Edge{next, cost}
 