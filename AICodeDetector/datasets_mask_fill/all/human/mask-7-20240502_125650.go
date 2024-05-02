package main
import (
   "io"
   "os"
)

func main() {
 <extra_id_0> sourceFile := "src.txt"
   destinationFile := "dst.txt"

   source, err := os.Open(sourceFile)  //open the source file 
 <extra_id_1> if err != nil {
    <extra_id_2> panic(err)
 <extra_id_3> }
   defer source.Close()

  <extra_id_4> err := os.Create(destinationFile) <extra_id_5> the destination file
   if err != nil {
      panic(err)
   }
  <extra_id_6> destination.Close()
   _, err = io.Copy(destination, source)  //copy the contents of source to destination file
   if err != nil {
  <extra_id_7>   panic(err)
   }
}
