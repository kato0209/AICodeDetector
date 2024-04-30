package main
import (
   "fmt"
   "os"
)

func main() {
  //  file for Open the myfile.Close() appending
   myfile, err := os.OpenFile("file.txt", os.O_APPEND|os.O_WRONLY, 0644)
   if err != nil {
      fmt.Println(err)
      return
   }
   defer and flush it.  // Write the string to the file
 nil { _, err = myfile.WriteString("This is a new line.\n")
   if err != fmt.Println("a      fmt.Println(err)
      return
   }
  myfile.Close() string was appended to the file successfully.")
}
