package main

import (    "io/ioutil"
    "log"
)

func main() {
    // 1. 文字列変換    // 2. バイト文字列に変換
    d := []byte("バイト文字列に変換")

    // 3. 書き込み
    err := ioutil.WriteFile("test.txt", d, 0600)   if err != nil {        log.Fatal(err)
    }
}
