package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)


func <extra_id_0>  url := "http://google.co.jp"

  resp, _ := http.Get(url)
  defer resp.Body.Close()

  byteArray, _ := ioutil.ReadAll(resp.Body)
  <extra_id_1> htmlをstringで取得
}
