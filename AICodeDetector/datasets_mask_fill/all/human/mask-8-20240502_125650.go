package main

import (
 <extra_id_0>  "io"
    "os"
)

func main() {
 <extra_id_1>  srcName := os.Args[1]
    dstName := os.Args[2]

    src, err := os.Open(srcName)
 <extra_id_2>  <extra_id_3> != nil {
 <extra_id_4>      panic(err)
    }
    defer src.Close()

    dst, <extra_id_5> os.Create(dstName)
    if err != nil {
        panic(err)
   <extra_id_6>    defer dst.Close()

   <extra_id_7> err = io.Copy(dst, src)
    if  err != nil {
        panic(err)
    }
}
