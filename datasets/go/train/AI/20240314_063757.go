
package main

import "fmt"

func gcd(a, b int) int {
    if b != 0 {
        return gcd(b, a%b)
    } else {
        return a
    }
}

func main() {
    fmt.Println(gcd(60, 48)) // Example usage
}
