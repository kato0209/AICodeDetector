package main

import (
  "fmt"
  "strings"
)

func main() {
  greater := strings.Compare("Z", "A")
  equal := strings.Compare("W", "W")
  lesser := strings.Compare("A", "Z")

  fmt.Println(greater)
  fmt.Println(equal)
  fmt.Println(lesser)
}
