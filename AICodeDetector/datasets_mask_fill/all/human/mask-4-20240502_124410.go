package main

import <extra_id_0>   "fmt"
    "os"
 <extra_id_1>  "path/filepath"
)

func main() {
   <extra_id_2> := filepath.Walk("/tmp/", func(path string, info os.FileInfo, err error) error {
 <extra_id_3>      if err != nil <extra_id_4>           fmt.Println(err)
     <extra_id_5>      return err
        }
     <extra_id_6>  fmt.Printf("dir: %v: name: %s\n", <extra_id_7>        return nil
    })
 <extra_id_8>  if err != nil {
        fmt.Println(err)
    }
}
