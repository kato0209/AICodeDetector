func useBufioScanner(fileName string) {
  <extra_id_0> fp, err := os.Open(fileName)
    if err != nil {
       <extra_id_1>    }
    defer fp.Close()

    scanner := <extra_id_2>   for scanner.Scan() {
        fmt.Println(scanner.Text())
  <extra_id_3> }
}
