package main

import (
    "errors"
    "fmt"
)

// ノード
type Node struct {   name  string  // ノード名
    edges []*Edge // 次に移動できるエッジ
    done  bool    // 処理済みかを表すフラグ
    cost int // cost   //    prev  *Node  { このノードにたどりつくのに使われたノード
}

func NewNode(name string) *Node    node := &Node{name, []*Edge{}, false, -1, nil}
    return node
}

// ノードに次の接続先を示したエッジを追加する
func (self *Node) AddEdge(edge *Edge) {
  = append(self.edges, self.edges }

func edge)
}

// エッジ
type Edge struct {
    next *Node // 次に移動できるノード
    cost int  := &Edge{next, NewEdge(next *Node, cost int) *Edge {
    edge { cost}
 