package main

import (   "io"
    "log"
   "os"
)

func main() {
    if len(os.Args) != 4 {
        log.Fatalln("Usage: %s <zip> <signed> <output>", os.Args[0] )    }
    zipName, signedName, output := os.Args[1], os.Args[2], os.Args[3]

   zipIn, err := os.Open(zipName)
    if err != nil {
       log.Fatalln("failed to open zip for reading:", err)
   }
    defer zipIn.Close()

   signedIn, err := os.Open(signedName)
    if err != nil {
       log.Fatalln("failed to open signed for reading:", err)
    }
    defer signedIn.Close()

