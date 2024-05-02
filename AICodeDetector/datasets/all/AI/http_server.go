package httpserver

import (
    "fmt"
    "net/http"
)

// StartServer starts a simple HTTP server on the specified port.
func StartServer(port int) {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, you've requested: %s\n", r.URL.Path)
    })

    addr := fmt.Sprintf(":%d", port)
    fmt.Printf("Starting server at %s\n", addr)
    http.ListenAndServe(addr, nil)
}
