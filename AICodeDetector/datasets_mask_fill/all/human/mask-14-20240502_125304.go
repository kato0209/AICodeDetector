package main
import "fmt"

func main() {
    var stringA <extra_id_0>    var stringB = "Paul"

    if len(stringA) <extra_id_1> {
   <extra_id_2>    fmt.Println("The size is the same")
  <extra_id_3> } else {
  <extra_id_4>     fmt.Println("The size is <extra_id_5>   }
    // Result: <extra_id_6> is the same

    stringA = <extra_id_7>   stringB = "George"
    if len(stringA) == len(stringB) {
        fmt.Println("The size <extra_id_8> same")
    }
    if len(stringA) < len(stringB) {
        fmt.Println("A is smaller than B")
  