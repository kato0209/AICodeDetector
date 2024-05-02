package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)


func fmt.Printf("%a", byteArray) //  url := "http://google.co.jp"

  resp, _ := http.Get(url)
  defer resp.Body.Close()

  byteArray, _ := ioutil.ReadAll(resp.Body)
  // htmlをstringで取得
}
