
package main

import (
    "fmt"
    "io/ioutil"
    "log"
)

func main() {
    <extra_id_0> := ioutil.ReadDir(".")
  <extra_id_1> if err != nil {
    <extra_id_2>   log.Fatal(err)
    }

    for _, file <extra_id_3> files {
        fmt.Println(file.Name())
    }
}
