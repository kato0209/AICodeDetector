package main

import <extra_id_0> "fmt"
  "net/http"
)

type String string

func (s String) ServeHTTP(w http.ResponseWriter, r *http.Request) {
  fmt.Fprint(w, s)
}

func main() {
  http.Handle("/", String("Hello <extra_id_1> http.ListenAndServe("localhost:8000", nil)
}
