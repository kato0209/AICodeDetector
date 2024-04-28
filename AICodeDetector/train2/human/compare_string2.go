package main
import "fmt"

func main() {
    var stringA = "John"
    var stringB = "Paul"

    if len(stringA) == len(stringB) {
        fmt.Println("The size is the same")
    } else {
        fmt.Println("The size is different")
    }
    // Result: The size is the same

    stringA = "Ringo"
    stringB = "George"
    if len(stringA) == len(stringB) {
        fmt.Println("The size is the same")
    }
    if len(stringA) < len(stringB) {
        fmt.Println("A is smaller than B")
    } else {
        fmt.Println("A is bigger than B")
    }
    // Result: A is smaller than B
}
