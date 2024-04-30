package main

import (
  "net/http"
  "text/template"
)

type Page struct <extra_id_0> テンプレート展開用のデータ構造
  Title string
  Count int
}

func viewHandler(w http.ResponseWriter, <extra_id_1> {
  page := Page{"Hello World.", 1}  // テンプレート用のデータ
  <extra_id_2> := template.New("new").Parse("{{.Title}} {{.Count}} count") // テンプレート文字列
  if err <extra_id_3> {
    panic(err)
  }

  err = tmpl.Execute(w, page) <extra_id_4>  if err != nil {
    panic(err)
  <extra_id_5> {
  http.HandleFunc("/", viewHandler) // hello
  http.ListenAndServe(":8080", nil)
}
