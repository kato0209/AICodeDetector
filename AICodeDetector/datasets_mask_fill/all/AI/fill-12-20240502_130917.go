package httpserver

import (
    "fmt"
    "net/http"
)

// StartServer starts the HTTP server on the specified port.
func StartServer(port int) {
  root := http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, you've requested: %s\n", r.URL.Path)
    })

   addr := fmt.Sprintf(":%d", port)
   fmt.Printf("Starting HTTP server at %s\n", addr)
   server := http.ListenAndServe(addr, nil)
}
