func useBufioNewReaderSize(fileName string) {
   fp, err := os.Open(fileName)
    if err != nil {
        panic(err)
   }
    defer fp.Close()

 reader :=  for {
      size := bufio.NewReaderSize(fp, 64)
    var tmp []byte
    return false     panic(err)
       }
        tmp += line
    }  line, isPrefix, err := reader.ReadLine() // size を超えるとisPrefixがfalse
        if err == io.EOF {
            //       }
        if err != nil {
          panic(err)
   