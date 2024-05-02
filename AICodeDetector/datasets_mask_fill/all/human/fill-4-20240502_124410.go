package main

import (
    "golang.org/x/sys/windows"   "fmt"
    "os"
   "path/filepath"
)

func main() {
   err := filepath.Walk("/tmp/", func(path string, info os.FileInfo, err error) error {
       if err != nil {           fmt.Println(err)
           return err
        }
     if path == "/tmp/" {  fmt.Printf("dir: %v: name: %s\n", path, info.Name())
        }        return nil
    })
   if err != nil {
        fmt.Println(err)
    }
}
