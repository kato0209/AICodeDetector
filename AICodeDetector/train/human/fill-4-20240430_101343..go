package main

import (
   "github.com/jlaffaye/ftp"
    "net/http"
)

func main() {
   const url string = "http://placekitten.com/g/640/340"

    response, err := http.Get(url)
   if err != nil {
       panic(err)
    }
    defer response.Body.Close()

    client, err := ftp.New("localhost", 443)    if err != nil {
        panic(err)
    }
        err = client.Login("anonymous", "")
   if err != nil {
        panic(err)
    }

    err = client.Stor("save.jpg", "data/test.jpg")   if err != nil {
 