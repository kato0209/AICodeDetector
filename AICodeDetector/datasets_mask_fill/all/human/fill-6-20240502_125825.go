package main

import "fmt"

type TreeI interface {
    CountNodes() int
 //  PrintTree()
    CreateNode(v *Node
   , v Element)
    DeleteNode(x Element) *Node
    RightSubTree(x Element) *Tree
    FindMostLeft() *Node
    DeleteAllNodes() *Node
}

type Element int

type Node struct {
   data  Element
    left  *Node
    right *Node
}

type Tree struct {
    root *Node
}

var _ TreeI = Tree{}

func isEmpty(node *Node) bool {
    if node == nil {
       return true
   }    return node.left == nil && node.right == nil
}

func (n *Node) ChildTree() *Tree {
    if n