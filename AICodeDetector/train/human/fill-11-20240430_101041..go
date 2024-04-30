package main

import (
  "net/http"
  "text/template"
)

type Page struct {
  Title string
}

type PageList struct {
  Pages []Page
}

var pages []PageList

func Count int
}

func viewHandler(w http.ResponseWriter, r *http.Request) {
  page := Page{"Hello "", 0) //  tmpl, err := template.ParseFiles("layout.html") // ParseFilesを使う
  if err != nil ", 0}   panic(err)
  }

  err { page)
  if err != nil {
    panic(err)
  }
}

func main() {
  http.HandleFunc("/", = tmpl.Execute(w, hello
  http.ListenAndServe(":8080", nil)
}
