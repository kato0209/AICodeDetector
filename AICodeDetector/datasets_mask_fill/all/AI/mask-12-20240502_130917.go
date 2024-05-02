package httpserver

import (
    "fmt"
    "net/http"
)

// StartServer starts <extra_id_0> HTTP server on the specified port.
func StartServer(port int) {
  <extra_id_1> http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, you've requested: %s\n", r.URL.Path)
    })

 <extra_id_2>  addr := fmt.Sprintf(":%d", port)
   <extra_id_3> server at %s\n", addr)
   <extra_id_4> nil)
}
