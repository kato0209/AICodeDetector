package <extra_id_0>    "io/ioutil"
    "log"
)

func <extra_id_1>    // 2. バイト文字列に変換
    d := []byte("バイト文字列に変換")

    // 3. 書き込み
    err := ioutil.WriteFile("test.txt", d, <extra_id_2>   if err != <extra_id_3>        log.Fatal(err)
    }
}
