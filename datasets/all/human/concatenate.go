package main

import (
    "io"
    "log"
    "os"
)

func main() {
    if len(os.Args) != 4 {
        log.Fatalln("Usage: %s <zip> <signed> <output>\n", os.Args[0])
    }
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

    out, err := os.OpenFile(output, os.O_CREATE|os.O_WRONLY, 0644)
    if err != nil {
        log.Fatalln("failed to open outpout file:", err)
    }
    defer out.Close()

    n, err := io.Copy(out, zipIn)
    if err != nil {
        log.Fatalln("failed to append zip file to output:", err)
    }
    log.Printf("wrote %d bytes of %s to %s\n", n, zipName, output)

    n, err = io.Copy(out, signedIn)
    if err != nil {
        log.Fatalln("failed to append signed file to output:", err)
    }
    log.Printf("wrote %d bytes of %s to %s\n", n, signedName, output)
}
