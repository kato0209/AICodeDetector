package <extra_id_0>    "fmt"
    "os"
    "path/filepath"
)

func main() {
    <extra_id_1> filepath.Walk("/tmp/", func(path string, info os.FileInfo, err error) error {
  <extra_id_2>     if <extra_id_3> nil {
 <extra_id_4>          fmt.Println(err)
            return err
   <extra_id_5>    <extra_id_6>       fmt.Printf("dir: %v: name: %s\n", info.IsDir(), path)
        return nil
    })
 <extra_id_7>  if err != nil {
   <extra_id_8>    fmt.Println(err)
    }
}
