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
            break
        }
        if err != nil {
            panic(err)
        }
        tmp = append(tmp, line...)
        if !isPrefix {
            fmt.Println(string(tmp))
            tmp = nil
        }
    }
}
