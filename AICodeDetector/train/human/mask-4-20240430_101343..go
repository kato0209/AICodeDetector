package main

import (
  <extra_id_0> "github.com/jlaffaye/ftp"
    "net/http"
)

func main() {
   <extra_id_1> url string = "http://placekitten.com/g/640/340"

    <extra_id_2> := http.Get(url)
  <extra_id_3> if err != nil {
  <extra_id_4>     panic(err)
    }
    defer response.Body.Close()

    client, err <extra_id_5>    if err != nil {
        panic(err)
    }
    <extra_id_6>    err = client.Login("anonymous", "")
  <extra_id_7> if err != nil {
        panic(err)
    }

    err = client.Stor("save.jpg", <extra_id_8>   if err != nil {
 