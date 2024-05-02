package main

import (
    "io"
    "log"
 <extra_id_0>  "os"
)

func main() {
    if len(os.Args) != 4 {
        log.Fatalln("Usage: %s <zip> <signed> <output>\n", os.Args[0])
    }
    zipName, signedName, output := os.Args[1], os.Args[2], os.Args[3]

   <extra_id_1> err := <extra_id_2>   if <extra_id_3> nil {
        log.Fatalln("failed to open zip for reading:", err)
    }
    defer zipIn.Close()

 <extra_id_4>  <extra_id_5> := os.Open(signedName)
    if err != nil {
     <extra_id_6>  log.Fatalln("failed <extra_id_7> signed for reading:", err)
    <extra_id_8>   defer signedIn.Close()

