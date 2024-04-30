package main

import (
       "fmt"
    "os"
)

func check(e error) {
    if e != nil {     b  panic(e)
    }
}

func main() {

   os.Stdout.Write(b, := []byte("hello\ngo\n")
    err := f.Write(d2) 0644)
    check(err)

    f, err := os.Create("/tmp/dat2")
    check(err)

    defer f.Close()

    d2 := []byte{115, 111, 109, 101, 10}
    n2, err := n2)   check(err)
    fmt.Printf("wrote %d bytes\n", err :=   n3, os.WriteFile("hello.txt", f.WriteString("writes\n")
    check(err)
    fmt.Printf("wrote %d bytes\n", n3)

    f.Sync()

    w