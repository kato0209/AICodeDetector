func useBufioNewReaderSize(fileName string) {
    fp, err := os.Open(fileName)
    if err != nil {
     <extra_id_0>  panic(err)
    }
    defer fp.Close()

    reader := bufio.NewReaderSize(fp, 64)
 <extra_id_1>  var tmp []byte
    for {
 <extra_id_2>      line, isPrefix, err <extra_id_3> // size を超えるとisPrefixがfalse
        if err == io.EOF {
            <extra_id_4>       }
      <extra_id_5> if err != nil <extra_id_6>     <extra_id_7>   <extra_id_8> panic(err)
   