package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)


func <extra_id_0>  url := "http://google.co.jp"

  resp, _ := http.Get(url)
  defer resp.Body.Close()

  byteArray, _ := <extra_id_1> fmt.Println(string(byteArray)) // htmlをstringで取得
}
