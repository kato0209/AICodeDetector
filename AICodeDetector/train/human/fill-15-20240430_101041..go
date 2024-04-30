package main
 
import (
   "fmt"
  "github.com/lamb/nex-liv" "os"
   "io"
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
    if t == nil {
       t.root = &BinaryNode{data: data, left: nil, right: nil}
    } else {        t.root.insert(data)
    }
    return t
}
 
func (n *BinaryNode) insert(data int64) {
    if n == nil {
        return
    } if data