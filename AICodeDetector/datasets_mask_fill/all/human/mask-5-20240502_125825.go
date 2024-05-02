package main

import(
  "fmt"
  "os"
) 

func <extra_id_0>    file,err := os.OpenFile("example.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
    
 <extra_id_1>  if err != nil {
		  fmt.Println("Could not open example.txt")
   <extra_id_2>  return
	  <extra_id_3> defer file.Close()
	 
    _, err2 := file.WriteString("Appending <extra_id_4> to example.txt")

	  if err2 != nil {
		  fmt.Println("Could not write <extra_id_5> example.txt")
      
	  }else{
    <extra_id_6> fmt.Println("Operation successful! Text has been appended to example.txt")
    }
}
