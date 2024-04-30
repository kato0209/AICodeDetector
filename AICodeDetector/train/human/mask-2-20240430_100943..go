package main

import (
   <extra_id_0>    "os"
)

func main() {
    srcName := <extra_id_1>   dstName := os.Args[2]

    src, <extra_id_2> os.Open(srcName)
    if err <extra_id_3> {
        panic(err)
  <extra_id_4> }
    defer src.Close()

    dst, err := <extra_id_5>   if err != <extra_id_6>        panic(err)
    }
    defer dst.Close()

    _, err = io.Copy(dst, src)
    if  err != nil {
     <extra_id_7>  panic(err)
    }
}
