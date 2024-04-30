package main

import (
    <extra_id_0>   "fmt"
    <extra_id_1> error) {
    if e != <extra_id_2>     <extra_id_3>  panic(e)
    }
}

func main() {

   <extra_id_4> := []byte("hello\ngo\n")
    err := <extra_id_5> 0644)
    check(err)

    f, err := os.Create("/tmp/dat2")
    check(err)

    defer f.Close()

    d2 := []byte{115, 111, 109, 101, 10}
    n2, err := <extra_id_6>   check(err)
    fmt.Printf("wrote %d bytes\n", <extra_id_7>   n3, <extra_id_8> f.WriteString("writes\n")
    check(err)
    fmt.Printf("wrote %d bytes\n", n3)

    f.Sync()

    w