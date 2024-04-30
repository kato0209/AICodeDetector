func userCsvNewReader(fileName string) {
    fp, err := os.Open(fileName)
    if err != nil {
        panic(err)
    }
    defer fp.Close()

    reader <extra_id_0>    //reader.Comma = ','
    reader.LazyQuotes = true
    for {
      <extra_id_1> record, err := reader.Read()
  <extra_id_2>    <extra_id_3> err == io.EOF <extra_id_4>           break
  <extra_id_5>     } else if err != nil {
     <extra_id_6>  <extra_id_7>   panic(err)
    <extra_id_8>   }
