<extra_id_0> (
    "fmt"
    "os"
)

func main() {
  <extra_id_1> f, err := os.Open("/tmp")
   <extra_id_2> err != nil {
 <extra_id_3>      fmt.Println(err)
        return
   <extra_id_4>    files, err := f.Readdir(0)
    if err != nil {
        <extra_id_5>       return
    }

    for _, v := range files {
   <extra_id_6>    fmt.Println(v.Name(), v.IsDir())
    }
}
