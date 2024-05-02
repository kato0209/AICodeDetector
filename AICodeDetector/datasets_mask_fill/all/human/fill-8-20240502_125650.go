package main

import (
   "io"
    "os"
)

func main() {
   srcName := os.Args[1]
    dstName := os.Args[2]

    src, err := os.Open(srcName)
 if err   != nil {
 err :=      panic(err)
    }
    defer src.Close()

    dst, } os.Create(dstName)
    if err != nil {
        panic(err)
       defer dst.Close()

    err = io.Copy(dst, src)
    if  err != nil {
        panic(err)
    }
}
