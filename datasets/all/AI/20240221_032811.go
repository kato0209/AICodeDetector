package main

import (
    "fmt"
    "os"
)

func copyFile(src, dst string) error {
    srcFile, err := os.Open(src)
    if err != nil {
        return err
    }
    defer srcFile.Close()

    dstFile, err := os.Create(dst)
    if err != nil {
        return err
    }
    defer dstFile.Close()

    _, err = io.Copy(dstFile, srcFile)
    if err != nil {
        return err
    }

    return nil
}

func main() {
    err := copyFile("source.txt", "destination.txt")
    if err != nil {
        fmt.Println("Error copying file:", err)
        return
    }

    fmt.Println("File copied successfully!")
}