<extra_id_0> (
    "io"
   <extra_id_1> main() {
    srcName := os.Args[1]
    dstName := os.Args[2]

    src, err := os.Open(srcName)
    if err != nil {
        panic(err)
    }
  <extra_id_2> defer src.Close()

    dst, err := <extra_id_3>   if err <extra_id_4> {
 <extra_id_5>  <extra_id_6>   panic(err)
    }
    defer dst.Close()

  <extra_id_7> _, err = io.Copy(dst, src)
    if  err != nil {
        panic(err)
    }
}
