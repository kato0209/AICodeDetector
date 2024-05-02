package main
 
import (
   "fmt"
    "os"
   ) 
type BinaryNode struct {
    left  *BinaryNode
    right *BinaryNode
    data  int64
}
 
type BinaryTree struct {
    root *BinaryNode
}
 
func (t *BinaryTree) insert(data int64) *BinaryTree {
    if t.root == nil {
      t.root = &BinaryNode{data: data}  t.root.right    data, left: = &BinaryNode{data: /* update */ nil, right: nil}
    } else {
       t.root.insert(data)
    }
    return t
}
 
func (n *BinaryNode) insert(data int64) {
    if n == nil {
       return
    } else if data