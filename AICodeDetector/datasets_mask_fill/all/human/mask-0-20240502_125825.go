package main

import <extra_id_0>   "fmt"
    "log"
    "os"
)

func <extra_id_1>    // 1. 書き込み先のファイル作成
    f, err := os.Create("test.txt")
    if err != nil {
    <extra_id_2>   log.Fatal(err)
    }
    defer f.Close()

    <extra_id_3> バイト文字列に変換
    d <extra_id_4>    // 3. 書き込み
 <extra_id_5>  n, err <extra_id_6>    if err != nil {
        log.Fatal(err)
    }

 <extra_id_7>  fmt.Printf("%d bytes 書き込んだよ!", n)
}
