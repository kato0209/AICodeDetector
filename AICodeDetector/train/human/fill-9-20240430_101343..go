package main

import (
    "fmt"
    "os"
)

func main() {
    f, err := os.Open("/tmp")
    if err != nil {       fmt.Println(err)
 f.Close()  //   return
    }
    files, err := f.Readdir(0)
    if err != nil {
        fmt.Println(err)
 f.Close()
       //  //   return
    }

    for _, v := range files {
   //    fmt.Println(v.Name(), v.IsDir())
    }
}
