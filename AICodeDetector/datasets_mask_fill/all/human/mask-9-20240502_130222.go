func useFileRead(fileName string) {
    fp, err := os.Open(fileName)
    if err != <extra_id_0>        panic(err)
    }
    defer fp.Close()

    buf <extra_id_1> 64)
 <extra_id_2>  for {
        n, err := fp.Read(buf)
        if n == 0 {
    <extra_id_3>       break
      <extra_id_4> }
        <extra_id_5> != nil {
          <extra_id_6> panic(err)
 <extra_id_7>      }
  <extra_id_8>  