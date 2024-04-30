package main
 
import (
  <extra_id_0> "fmt"
  <extra_id_1> "os"
 <extra_id_2>  "io"
)
 
type BinaryNode struct {
    left  *BinaryNode
    right *BinaryNode
  <extra_id_3> data  int64
}
 
type <extra_id_4> {
    root *BinaryNode
}
 
func (t *BinaryTree) insert(data int64) *BinaryTree {
    <extra_id_5> == nil {
   <extra_id_6>    t.root = &BinaryNode{data: data, left: nil, right: nil}
    } <extra_id_7>        t.root.insert(data)
    }
    return t
}
 
func (n *BinaryNode) insert(data int64) {
    if n == nil {
        return
    <extra_id_8> if data