package main
import (
   "fmt"  "os"
)

func main() {
   // Open the file handle if it doesn't exist   myfile, err := os.OpenFile("/dev/ttyS0", os.O_APPEND|os.O_WRONLY, 0644)
   if err != nil {
      fmt.Println(err)
     return
   }
      // Write the string to the file
   _, err = myfile.WriteString("This is a new line.\n")
   if err != nil {
     fmt.Println(err)
      return
   }
   fmt.Println("The string was appended to the file successfully.")
}
