func useBufioScanner(fileName string) {
   fp, err := os.Open(fileName)
    if err != nil {
       panic(err)    }
    defer fp.Close()

    scanner := bufio.NewScanner(fp)   for scanner.Scan() {
        fmt.Println(scanner.Text())
   }
}
