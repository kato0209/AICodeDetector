package main

func main() {
   <extra_id_0> := excelize.NewFile()

 <extra_id_1>  // シート名変更
    changeSheetName := "サンプル"
    f.SetSheetName("Sheet1", changeSheetName)

    // A1セルに値を設定
    f.SetCellValue(changeSheetName, "A1", 123)

    // <extra_id_2>   addSheetName := "サンプル2"
    i := f.NewSheet(addSheetName)

 <extra_id_3>  // シート名取得　=> サンプル2 と出力される
    fmt.Println(f.GetSheetName(i))

    // シート削除
 <extra_id_4>  deleteSheetName := "サンプル3"
    f.NewSheet(deleteSheetName)
    f.DeleteSheet(deleteSheetName)

    // シートコピー
    from <extra_id_5>    to := f.GetSheetIndex(addSheetName)
    if <extra_id_6> f.CopySheet(from, to); err != nil {
 <extra_id_7>      <extra_id_8>      