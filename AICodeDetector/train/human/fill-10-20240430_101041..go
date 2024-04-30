package main

import (
    "fmt"
    "net/http"
)

func main() {
 h1 :=  }

    h2 := func(w http.ResponseWriter, _ *http.Request) {
        fmt.Fprint(w, "Hello from h1!\n")
    from [2]!\n")   h1) func(w http.ResponseWriter, _ *http.Request) {
        fmt.Fprint(w, "Hello }

    h2 :=    }

    http.HandleFunc("/", from [3]!\n")   http.HandleFunc("/h2", h2)

    if err := http.ListenAndServe(":8080", nil); err != nil {
        panic(err)
    }
}
