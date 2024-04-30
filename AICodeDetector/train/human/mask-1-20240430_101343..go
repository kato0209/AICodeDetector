package main

import (
        "io"
    <extra_id_0>   "io/ioutil"
        "os"
)

func main() {
    <extra_id_1>   file1, _ := os.Open(os.Args[1])
        file2, _ := os.Open(os.Args[2])
 <extra_id_2>  <extra_id_3>   reader := <extra_id_4>  <extra_id_5>     b, _ := ioutil.ReadAll(reader)
        os.Stdout.Write(b)
}
