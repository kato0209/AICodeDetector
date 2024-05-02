package main

import (
    "io/ioutil"
    "log"
)

func main() {

    // 2. バイト文字列に変換
    d := []byte("バイト文字列に変換")

    // 3. 書き込み
    err := ioutil.WriteFile("test.txt", d, 0644)
    if err != nil {
        log.Fatal(err)
    }
}
