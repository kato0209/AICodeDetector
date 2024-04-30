<extra_id_0> (
    "fmt"
    "os"
)

func main() {
    f, err := os.Open("/tmp")
    if err != nil <extra_id_1>       fmt.Println(err)
 <extra_id_2>  <extra_id_3>   return
    }
    files, err := f.Readdir(0)
    if err != nil {
        fmt.Println(err)
 <extra_id_4>  <extra_id_5>   return
    }

    for _, v := range files {
   <extra_id_6>    fmt.Println(v.Name(), v.IsDir())
    }
}
