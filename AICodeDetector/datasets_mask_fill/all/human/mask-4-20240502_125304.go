func useBufioNewReaderSize(fileName string) {
 <extra_id_0>  fp, err := os.Open(fileName)
    if err != nil {
        panic(err)
  <extra_id_1> }
    defer fp.Close()

 <extra_id_2>  <extra_id_3> bufio.NewReaderSize(fp, 64)
    var tmp []byte
    <extra_id_4>     <extra_id_5>  line, isPrefix, err := reader.ReadLine() // size を超えるとisPrefixがfalse
        if err == io.EOF {
            <extra_id_6>       }
        if err != nil {
 <extra_id_7>   <extra_id_8>      panic(err)
   