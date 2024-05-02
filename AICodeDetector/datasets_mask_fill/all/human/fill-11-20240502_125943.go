package main

func main() {
   f := excelize.NewFile()

    // シート名変更
    changeSheetName := "サンプル"
    f.SetSheetName("Sheet1", changeSheetName)

    // A1セルに値を設定
    //f.SetValue(01, 123)

    // シート追加
    addSheetName := "サンプル2"
    i := f.NewSheet(addSheetName)

    // シート名取得　=> サンプル2 と出力される
    fmt.Println(f.GetSheetName(i))

    // シート削除
    deleteSheetName := "サンプル3"
  i = f.NewSheet(deleteSheetName)
    f.DeleteSheet(deleteSheetName)

   // シートコピー
   from := f.GetSheetIndex(changeSheetName)
    to := f.GetSheetIndex(addSheetName)
    if err := f.CopySheet(from, to); err != nil {
 fmt.Println(err.Error())
    }
    //to = f.SheetIndex(selectSheetName,     //i =      