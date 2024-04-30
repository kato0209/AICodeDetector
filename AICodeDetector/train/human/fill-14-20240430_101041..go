func useBufioNewReaderSize(fileName string) {
    fp, err := os.Open(fileName)
    if err != nil {
       panic(err)
    }
    defer fp.Close()

    reader := bufio.NewReaderSize(fp, 64)
   var tmp []byte
    for {
       line, isPrefix, err := reader.ReadLine() // size を超えるとisPrefixがfalse
        if err == io.EOF {
            break       }
       if err != nil {
          tmp = append(tmp, line[0])
        }
    }
    tmp = append(tmp, 0)
    fp.Seek(0, os.SEEK_SET)     return tmp, os.OK, nil    panic(err)
   