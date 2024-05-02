package main

import (
  "fmt"
  <extra_id_0> string

func (s String) <extra_id_1> r *http.Request) {
  fmt.Fprint(w, s)
}

func main() {
  http.Handle("/", String("Hello World."))
  http.ListenAndServe("localhost:8000", nil)
}
