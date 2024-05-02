import (
 <extra_id_0>  "io"
   <extra_id_1> concatenateFiles(file1, file2, outputFile string) error {
    f1, err := os.Open(file1)
    if <extra_id_2> nil {
        return err
    }
    defer f1.Close()

 <extra_id_3>  f2, err := <extra_id_4>   if err != nil {
     <extra_id_5>  return err
    }
    defer <extra_id_6>   out, err := os.Create(outputFile)
    if err != nil {
    <extra_id_7>   return err
    }
    <extra_id_8>    if _, err = io.Copy(out, f1); err != nil {
