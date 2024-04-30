package main

import (
  "net/http"
  "text/template"
)

type Page struct {
  Title <extra_id_0> Count int
}

func viewHandler(w http.ResponseWriter, r *http.Request) {
  page := Page{"Hello <extra_id_1>  tmpl, err := template.ParseFiles("layout.html") // ParseFilesを使う
  if err != nil <extra_id_2>   panic(err)
  }

  err <extra_id_3> page)
  if err != nil {
    panic(err)
  }
}

func main() {
  http.HandleFunc("/", <extra_id_4> hello
  http.ListenAndServe(":8080", nil)
}
