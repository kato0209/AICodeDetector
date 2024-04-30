package main
import (
   "fmt"
   "os"
)

func <extra_id_0>  <extra_id_1> Open the <extra_id_2> appending
   myfile, err := os.OpenFile("file.txt", os.O_APPEND|os.O_WRONLY, 0644)
   if err != nil {
      fmt.Println(err)
      return
   }
   defer <extra_id_3>  // Write the string to the file
 <extra_id_4> _, err = myfile.WriteString("This is a new line.\n")
   if err != <extra_id_5>      fmt.Println(err)
      return
   }
  <extra_id_6> string was appended to the file successfully.")
}
