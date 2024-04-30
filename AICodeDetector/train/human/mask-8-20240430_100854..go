package main

import <extra_id_0>   "io"
    "log"
 <extra_id_1>  "os"
)

func main() {
    if len(os.Args) != 4 {
        log.Fatalln("Usage: %s <zip> <signed> <extra_id_2>    }
    zipName, signedName, output := os.Args[1], os.Args[2], os.Args[3]

   <extra_id_3> err := os.Open(zipName)
    <extra_id_4> != nil {
 <extra_id_5>      log.Fatalln("failed to open zip for reading:", err)
 <extra_id_6>  }
    defer zipIn.Close()

  <extra_id_7> signedIn, err := os.Open(signedName)
    if err != nil {
   <extra_id_8>    log.Fatalln("failed to open signed for reading:", err)
    }
    defer signedIn.Close()

