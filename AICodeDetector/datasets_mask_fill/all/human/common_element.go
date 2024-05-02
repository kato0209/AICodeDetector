package main
import "fmt"

// function to get common elements 2. Golang Program to find the common elements from two arrays
func intersection(arr1, arr2 []string) []string {
   out := []string{}
   bucket := map[string]bool{}
   for _, i := range arr1 {
      for _, j := range arr2 {
         if i == j && !bucket[i] {
            out = append(out, i)
            bucket[i] = true
         }
      }
   }
   return out
}
func main() {
   arr1 := []string{"apple", "mango", "banana", "papaya"}
   fmt.Println("The first array entered is:", arr1)
   arr2 := []string{"cherry", "papaya", "mango"}
   fmt.Println("The second array entered is:", arr2)
   result := intersection(arr1, arr2)
   fmt.Println()
   fmt.Println("The common elements of the above two arrays are:", result)
}
