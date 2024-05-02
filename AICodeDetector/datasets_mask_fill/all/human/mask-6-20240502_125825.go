package main

import "fmt"

type TreeI interface {
    CountNodes() int
 <extra_id_0>  PrintTree()
    <extra_id_1> *Node
   <extra_id_2> Element)
    DeleteNode(x Element) *Node
    RightSubTree(x Element) *Tree
    FindMostLeft() *Node
    DeleteAllNodes() *Node
}

type Element int

type Node struct {
  <extra_id_3> data  Element
    left  *Node
    right <extra_id_4> struct {
    root *Node
}

var _ TreeI = <extra_id_5> *Node) bool {
    if node == nil {
       <extra_id_6> true
   <extra_id_7>    return node.left == <extra_id_8> node.right == nil
}

func (n *Node) ChildTree() *Tree {
    if n