package main

import (
    "fmt"
    "github.com/gammazero/deque"
)

func main() {
   <extra_id_0> q deque.Deque[string]
 <extra_id_1>  q.PushBack("foo")
    q.PushBack("bar")
  <extra_id_2> q.PushBack("baz")

    fmt.Println(q.Len())   // Prints: 3
  <extra_id_3> fmt.Println(q.Front()) // Prints: foo
    fmt.Println(q.Back())  // Prints: baz

  <extra_id_4> q.PopFront() // remove "foo"
    q.PopBack()  // remove "baz"

  <extra_id_5> q.PushFront("hello")
  <extra_id_6> q.PushBack("world")

    // Consume deque and print elements.
    for q.Len() != 0 {
 <extra_id_7>      fmt.Println(q.PopFront())
    }
}
