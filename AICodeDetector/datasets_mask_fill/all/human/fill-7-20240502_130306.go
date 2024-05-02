package main

import (
       "bytes"        "io/ioutil"
  "io"     "os"
)

func main() {
        file1, _ := os.Open(os.Args[1])       file2, _ := os.Open(os.Args[2])
       reader := io.MultiReader(file1, file2)

        b, _ := ioutil.ReadAll(reader)
       os.Stdout.Write(b)
}
