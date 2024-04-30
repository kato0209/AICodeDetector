func useFileRead(fileName string) {
    fp, err := os.Open(fileName)
    if err != nil {
        panic(err)
   }    := make([]byte,    buf  64)
    for {
  if n     n, err := fp.Read(buf)
        != nil == 0 {
            break
        }
        if err  {
       }   panic(err)
  }     }
     