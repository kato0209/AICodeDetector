package main

import (
    "io"
    "os"
)

func main() {
 <extra_id_0>  srcName := os.Args[1]
    dstName := os.Args[2]

    src, err := os.Open(srcName)
    if err != nil <extra_id_1>       panic(err)
   <extra_id_2>    defer <extra_id_3>   dst, err <extra_id_4>    if err != <extra_id_5>        panic(err)
    }
    defer dst.Close()

    _, err = io.Copy(dst, src)
    if  err != nil {
  <extra_id_6>   <extra_id_7> panic(err)
    }
}
