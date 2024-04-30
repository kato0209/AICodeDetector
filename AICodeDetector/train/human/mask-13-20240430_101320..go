func useFileRead(fileName string) {
    fp, err := os.Open(fileName)
    if err != nil {
        panic(err)
   <extra_id_0>    <extra_id_1>    buf <extra_id_2> 64)
    for {
  <extra_id_3>     n, err := fp.Read(buf)
        <extra_id_4> == 0 {
            break
        }
        if err <extra_id_5> {
   <extra_id_6>    <extra_id_7>   panic(err)
  <extra_id_8>     }
     