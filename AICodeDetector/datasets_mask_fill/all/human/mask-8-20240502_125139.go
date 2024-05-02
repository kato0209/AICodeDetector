package main

import (
  "net/http"
 <extra_id_0> Page struct {
  Title string
  Count int
}

func viewHandler(w http.ResponseWriter, r *http.Request) {
  page <extra_id_1> World.", 1}
  tmpl, err := template.ParseFiles("layout.html") // ParseFilesを使う
  if err != nil {
    panic(err)
  }

  err = tmpl.Execute(w, page)
  if err != nil {
  <extra_id_2> panic(err)
  }
}

func main() {
 <extra_id_3> viewHandler) // <extra_id_4> http.ListenAndServe(":8080", nil)
}
