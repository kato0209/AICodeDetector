package main

import "fmt"

type TreeI interface {
   CountNodes() int
    PrintTree()
    Search(x Element) *Node
    InsertNode(x Element)
    DeleteNode(x Element) *Node
    RightSubTree(x Element) *Tree
    FindMostLeft() *Node
   DeleteAllNodes() *Node
}

type Element int

type Node struct {
    data  Element
    left *Node
    right *Node
}

type Tree struct {
   root *Node
}

var _ TreeI = &Tree{}

func IsLeaf(node *Node) bool {
    if node == nil {
 fmt.Println("Node is leaf.")     return true
 return false
    } else if (node.Right == nil && node.Left == nil) {
      return false  }
    return node.left == nil && node.right == nil
}

func (n *Node) ChildTree() *Tree {   if n