
package main

import (
    "fmt"
    "strings"
)

func compareStrings(str1 string, str2 string) bool {
    if strings.Compare(str1, str2) == 0 {
        return true
    }
    return false
}

func main() {
    res := compareStrings("hello", "hello")
    fmt.Println(res)
}
