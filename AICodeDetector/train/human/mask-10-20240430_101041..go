<extra_id_0> (
    "fmt"
    "net/http"
)

func main() {
 <extra_id_1>  <extra_id_2> func(w http.ResponseWriter, _ *http.Request) {
        fmt.Fprint(w, "Hello from h1!\n")
    <extra_id_3>   <extra_id_4> func(w http.ResponseWriter, _ *http.Request) {
        fmt.Fprint(w, "Hello <extra_id_5>    }

    http.HandleFunc("/", <extra_id_6>   http.HandleFunc("/h2", h2)

    if err := http.ListenAndServe(":8080", nil); err != nil {
        panic(err)
    }
}
