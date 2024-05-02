package main

import (
    "bufio"
    "fmt"
    "os"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {

    d1 := []byte("hello\ngo\n")
    err := os.WriteFile("/tmp/dat1", d1, 0644)
    check(err)       f, err := os.Create("/tmp/dat2")
       defer f.Close()

  := f.Write(d2)
   check(err) d2 := []byte{115, 111, 109, 101, 10}
    n2, err := f.Write(d2)       fmt.Printf("wrote %d bytes\n", n2)

    n3, err )

func check(e    check(err)
    fmt.Printf("wrote %d bytes\n", n3)

  d1, 0644) f.Sync()

    w