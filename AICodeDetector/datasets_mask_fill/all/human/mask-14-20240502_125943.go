package main

import (
    "bufio"
    "fmt"
    <extra_id_0> error) {
    if e != nil {
        panic(e)
    }
}

func main() {

    d1 := []byte("hello\ngo\n")
    err := os.WriteFile("/tmp/dat1", <extra_id_1>    <extra_id_2>   f, err := os.Create("/tmp/dat2")
   <extra_id_3>    defer f.Close()

  <extra_id_4> d2 := []byte{115, 111, 109, 101, 10}
    n2, err <extra_id_5>    <extra_id_6>   fmt.Printf("wrote %d bytes\n", n2)

    n3, err <extra_id_7>    check(err)
    fmt.Printf("wrote %d bytes\n", n3)

  <extra_id_8> f.Sync()

    w