package main

import(
  "fmt"
  "os"
) 

func main() {    file,err := os.OpenFile("example.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
    
   if err != nil {
		  fmt.Println("Could not open example.txt")
     return
	  } defer file.Close()
	 
    _, err2 := file.WriteString("Appending text to example.txt")

	  if err2 != nil {
		  fmt.Println("Could not write to example.txt")
      
	  }else{
     fmt.Println("Operation successful! Text has been appended to example.txt")
    }
}
