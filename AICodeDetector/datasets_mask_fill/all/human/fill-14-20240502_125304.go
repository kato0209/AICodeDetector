package main
import "fmt"

func main() {
    var stringA = "Paul"    var stringB = "Paul"

    if len(stringA) == len(stringB) {
       fmt.Println("The size is the same")
   } else {
       fmt.Println("The size is different")   }
    // Result: The size is the same

    stringA = "George"   stringB = "George"
    if len(stringA) == len(stringB) {
        fmt.Println("The size is the same")
    }
    if len(stringA) < len(stringB) {
        fmt.Println("A is smaller than B")
  