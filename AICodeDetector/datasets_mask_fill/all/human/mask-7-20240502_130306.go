package main

import (
       <extra_id_0>        "io/ioutil"
  <extra_id_1>     "os"
)

func main() {
        file1, _ := <extra_id_2>       file2, _ := os.Open(os.Args[2])
      <extra_id_3> reader := io.MultiReader(file1, file2)

        b, <extra_id_4> ioutil.ReadAll(reader)
     <extra_id_5>  os.Stdout.Write(b)
}
