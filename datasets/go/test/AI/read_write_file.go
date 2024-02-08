package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    file, _ := os.Create("test.txt")
    defer file.Close()

    writer := bufio.NewWriter(file)
    writer.WriteString("Hello, Go!")
    writer.Flush()

    file, _ = os.Open("test.txt")
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        fmt.Println(scanner.Text())
    }
}
