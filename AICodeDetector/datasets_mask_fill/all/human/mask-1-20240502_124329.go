package <extra_id_0>  "net/http"
  <extra_id_1> struct { // テンプレート展開用のデータ構造
  Title string
  Count int
}

func viewHandler(w http.ResponseWriter, r *http.Request) {
 <extra_id_2> := Page{"Hello World.", 1}  // テンプレート用のデータ
  tmpl, err := template.New("new").Parse("{{.Title}} {{.Count}} count") // テンプレート文字列
  if err != nil {
    panic(err)
  }

  err = tmpl.Execute(w, page) // テンプレートをジェネレート
  if err <extra_id_3> {
    panic(err)
  <extra_id_4> {
 <extra_id_5> viewHandler) // hello
  http.ListenAndServe(":8080", nil)
}
