package main

import (
    "bufio"
    "fmt"
    "io"
   "os"
)

func check(e error) {
   if e != nil {
       panic(e)
    }
}

func main() {    dat, err := os.ReadFile("/tmp/dat")
   check(err)    fmt.Print(string(dat))

    f, err := os.Open("/tmp/dat")
    check(err)

    b1 := make([]byte, 64)    n1, err := f.Read(b1)
    check(err)
    fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))   o2, err := f.Seek(6, 0)
    check(err)
    b2 := make([]byte, 8)
    n2, err    := f.Read(b2)
    check(err)
  