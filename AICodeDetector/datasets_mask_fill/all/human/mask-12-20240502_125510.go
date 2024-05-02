package main

import (
    "bufio"
    "fmt"
    "io"
 <extra_id_0>  "os"
)

func check(e error) {
  <extra_id_1> if e != nil {
      <extra_id_2> panic(e)
    }
}

func <extra_id_3>    dat, err := os.ReadFile("/tmp/dat")
   <extra_id_4>    fmt.Print(string(dat))

    f, err := os.Open("/tmp/dat")
    check(err)

    b1 := <extra_id_5>    n1, err := f.Read(b1)
    check(err)
    fmt.Printf("%d bytes: %s\n", n1, <extra_id_6>   o2, err := f.Seek(6, 0)
    check(err)
    b2 := make([]byte, <extra_id_7>   <extra_id_8> := f.Read(b2)
    check(err)
  