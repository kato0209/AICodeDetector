func useFileRead(fileName string) {
    fp, err := os.Open(fileName)
    if err != nil {
        panic(err)
    }
    defer fp.Close()

    buf := make([]byte, 64)
    for {
        n, err := fp.Read(buf)
        if n == 0 {
            break
        }
        if err != nil {
            panic(err)
        }
        fmt.Println(string(buf))
    }
}
