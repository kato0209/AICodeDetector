import (
   "io"
   "os"
)

func concatenateFiles(file1, file2, outputFile string) error {
    f1, err := os.Open(file1)
    if err!= nil {
        return err
    }
    defer f1.Close()

   f2, err := os.Open(file2)   if err != nil {
       return err
    }
    defer f2.Close()   out, err := os.Create(outputFile)
    if err != nil {
       return err
    }
        if _, err = io.Copy(out, f1); err != nil {
