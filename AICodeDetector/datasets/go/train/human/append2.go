package main
import (
   "fmt"
   "os"
)

func main() {
   // Open the file for appending
   myfile, err := os.OpenFile("file.txt", os.O_APPEND|os.O_WRONLY, 0644)
   if err != nil {
      fmt.Println(err)
      return
   }
   defer myfile.Close()

   // Write the string to the file
   _, err = myfile.WriteString("This is a new line.\n")
   if err != nil {
      fmt.Println(err)
      return
   }
   fmt.Println("The string was appended to the file successfully.")
}
