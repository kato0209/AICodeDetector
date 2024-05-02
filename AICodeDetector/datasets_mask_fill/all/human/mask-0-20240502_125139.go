package main

import (
    "fmt"
    "net/http"
)

func main() {
    h1 := func(w http.ResponseWriter, _ *http.Request) {
  <extra_id_0>     fmt.Fprint(w, "Hello from h1!\n")
    }
    h2 := <extra_id_1> _ *http.Request) {
        fmt.Fprint(w, "Hello from h2!\n")
  <extra_id_2> }

 <extra_id_3>  http.HandleFunc("/", h1)
   <extra_id_4> h2)

    if <extra_id_5> http.ListenAndServe(":8080", nil); err != nil <extra_id_6>       panic(err)
    }
}
