package main
import (
   "io"
   "os"
)

func main() {
  sourceFile := "src.txt"
   destinationFile := "dst.txt"

   source, err := os.Open(sourceFile)  //open the source file 
  if err != nil {
     panic(err)
  }
   defer source.Close()

  destination, err := os.Create(destinationFile) //create the destination file
   if err != nil {
      panic(err)
   }
  defer destination.Close()
   _, err = io.Copy(destination, source)  //copy the contents of source to destination file
   if err != nil {
     panic(err)
   }
}
