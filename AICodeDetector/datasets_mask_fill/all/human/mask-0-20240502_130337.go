package main

import (
 <extra_id_0>  "github.com/jlaffaye/ftp"
    "net/http"
)

func main() {
    var url string = "http://placekitten.com/g/640/340"

  <extra_id_1> response, <extra_id_2> http.Get(url)
    if err != nil {
        panic(err)
    <extra_id_3>   defer response.Body.Close()

  <extra_id_4> client, err := ftp.Connect("localhost:21")
    if err != nil {
        panic(err)
    }
    defer client.Quit()

  <extra_id_5> err = client.Login("anonymous", "")
    if <extra_id_6> nil {
    <extra_id_7>   panic(err)
    }

    err <extra_id_8> response.Body)
    if err != nil {
 