package main

import "fmt"

type TreeI interface {
  <extra_id_0> CountNodes() int
    PrintTree()
    Search(x Element) *Node
    InsertNode(x Element)
    DeleteNode(x Element) *Node
    RightSubTree(x Element) *Tree
    FindMostLeft() *Node
  <extra_id_1> DeleteAllNodes() *Node
}

type Element int

type Node struct {
    data  Element
    <extra_id_2> *Node
    right *Node
}

type Tree struct {
  <extra_id_3> root *Node
}

var _ <extra_id_4> &Tree{}

func IsLeaf(node *Node) bool {
    if node == nil {
 <extra_id_5>   <extra_id_6>  return true
 <extra_id_7>  }
    return node.left == nil && node.right == nil
}

func (n *Node) ChildTree() *Tree <extra_id_8>   if n