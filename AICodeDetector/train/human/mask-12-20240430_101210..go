<extra_id_0> string) {
   <extra_id_1> err := os.Open(fileName)
    if err != nil {
   <extra_id_2>    panic(err)
    }
    defer fp.Close()

    scanner := bufio.NewScanner(fp)
    for <extra_id_3>        fmt.Println(scanner.Text())
    }
}
