package main
 
import (
 <extra_id_0>  "fmt"
    "os"
   <extra_id_1> 
type BinaryNode struct {
    left  *BinaryNode
    right *BinaryNode
    data  int64
}
 
type <extra_id_2> {
    root *BinaryNode
}
 
func (t *BinaryTree) insert(data int64) *BinaryTree {
    if t.root == <extra_id_3>  <extra_id_4>    <extra_id_5> = &BinaryNode{data: <extra_id_6> nil, right: nil}
    } else {
      <extra_id_7> t.root.insert(data)
    }
    return t
}
 
func (n *BinaryNode) insert(data int64) {
    if n == nil {
 <extra_id_8>      return
    } else if data