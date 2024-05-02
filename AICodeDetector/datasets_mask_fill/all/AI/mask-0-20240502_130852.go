package fileops

import (
    "io"
    "os"
)

func CopyFile(src, dst string) error {
    source, err := os.Open(src)
  <extra_id_0> if err != nil {
  <extra_id_1>  <extra_id_2>  return err
    }
  <extra_id_3> defer source.Close()

 <extra_id_4>  destination, err := os.Create(dst)
    if err != nil {
     <extra_id_5>  return err
 <extra_id_6>  }
    defer destination.Close()

    _, err = io.Copy(destination, source)
    return err
}
