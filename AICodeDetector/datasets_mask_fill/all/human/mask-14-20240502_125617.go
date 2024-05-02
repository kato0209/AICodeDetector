func <extra_id_0>    slice := buffer[10:20]
  <extra_id_1> for i := 0; i < len(slice); i++ {
  <extra_id_2>     slice[i] = byte(i)
    }
    fmt.Println("before", slice)
    AddOneToEachElement(slice)
    fmt.Println("after", slice)
}
