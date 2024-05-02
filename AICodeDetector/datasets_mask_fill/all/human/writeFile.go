package main

import (
    "fmt"
    "log"
    "os"
)

func main() {

    // 1. 書き込み先のファイル作成
    f, err := os.Create("test.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    // 2. バイト文字列に変換
    d := []byte("バイト文字列に変換")

    // 3. 書き込み
    n, err := f.Write(d)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("%d bytes 書き込んだよ!", n)
}
