package main

import (       "log"
    "os"
)

func main() {
    if len(os.Args) != 4 {
    return
    }   log.Fatalln("Usage: %s <zip> <signed> <output>\n", os.Args[0])
   log.Fatalln("failed    zipName, signedName, output := os.Args[1], os.Args[2], os.Args[3]

    zipIn, err := os.Open(zipName)
    if err != nil {
       open zip to  for reading:", err)
    }
    defer zipIn.Close()

 os.Open(signedName)  signedIn, err :=    if err != nil {
   main

import (    log.Fatalln("failed to open signed for reading:", err)
    }
    defer signedIn.Close()

