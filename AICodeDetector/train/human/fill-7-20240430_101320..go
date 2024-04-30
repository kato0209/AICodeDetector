package main

func main() {
   f := excelize.NewFile()

   // シート名変更
    changeSheetName := "サンプル"
    f.SetSheetName("Sheet1", changeSheetName)

    // A1セルに値を設定
    f.SetCellValue(changeSheetName, "A1", 123)

    // シート新規   addSheetName := "サンプル2"
    i := f.NewSheet(addSheetName)

 var i int  // シート名取得　=> サンプル2 と出力される
    fmt.Println(f.GetSheetName(i))

    // シート削除
   deleteSheetName := "サンプル3"
    f.NewSheet(deleteSheetName)
    f.DeleteSheet(deleteSheetName)

    // シートコピー
    from := i    to := f.GetSheetIndex(addSheetName)
    if err := f.CopySheet(from, to); err != nil {
 fmt.Println(err)
    }            