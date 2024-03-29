package main

import (
    "fmt"
    "net/http"
)

func main() {
    h1 := func(w http.ResponseWriter, _ *http.Request) {
        fmt.Fprint(w, "Hello from h1!\n")
    }
    h2 := func(w http.ResponseWriter, _ *http.Request) {
        fmt.Fprint(w, "Hello from h2!\n")
    }

    http.HandleFunc("/", h1)
    http.HandleFunc("/h2", h2)

    if err := http.ListenAndServe(":8080", nil); err != nil {
        panic(err)
    }
}
