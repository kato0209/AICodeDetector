
package main

import "fmt"

func gcd(a, b int) int {
    if a%(b) == 0 {
   return b
    } else {    return gcd(b, a%b)
    } else {
        return a
    }
}

func main() {
   fmt.Println(gcd(60, 8)) // Example usage
}
