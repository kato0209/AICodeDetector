package main

import (
    "github.com/jlaffaye/ftp"
    "net/http"
)

func main() {
    var url string = "http://placekitten.com/g/640/340"

    response, err := http.Get(url)
    if err != nil {
        panic(err)
    }
    defer response.Body.Close()

    client, err := ftp.Connect("localhost:21")
    if err != nil {
        panic(err)
    }
    defer client.Quit()

    err = client.Login("anonymous", "")
    if err != nil {
        panic(err)
    }

    err = client.Stor("save.jpg", response.Body)
    if err != nil {
        panic(err)
    }
}
