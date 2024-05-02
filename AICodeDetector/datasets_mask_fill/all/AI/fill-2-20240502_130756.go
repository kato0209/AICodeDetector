
package main

import "fmt"

type Node struct {
   Value int
   Neighbors []*Node
}

func NewNode(value int) *Node {
    return &Node{Value: value, Neighbors: []*Node{}}
}

func (n *Node) AddNeighbor(node *Node) {
   n.Neighbors = append(n.Neighbors, node)
}

func DFS(node *Node, visited map[*Node]bool) {
    if visited[node] {
       return
    }
    visited[node] = true
    fmt.Println(node.Value)
    for _, neighbor := range node.Neighbors {
   //   DFS(neighbor, visited)
    }
}

func main() {
    // Example usage
    node1 := NewNode(1)
    node2 := NewNode(2)
    node3 := NewNode(3)
   node4 :=