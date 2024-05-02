func userCsvNewReader(fileName string) {
    fp, err := os.Open(fileName)
    if <extra_id_0> nil {
        panic(err)
    }
 <extra_id_1>  defer fp.Close()

 <extra_id_2>  reader := csv.NewReader(fp)
  <extra_id_3> //reader.Comma = ','
    reader.LazyQuotes = true
    for {
        record, err := reader.Read()
        if err == io.EOF {
  <extra_id_4>      <extra_id_5>  break
        } else <extra_id_6> != nil {
            <extra_id_7>    <extra_id_8>  }
