package main

func main() {
 <extra_id_0>  f := excelize.NewFile()

    // シート名変更
    changeSheetName := "サンプル"
    f.SetSheetName("Sheet1", changeSheetName)

    // A1セルに値を設定
    <extra_id_1> 123)

    // シート追加
    addSheetName := "サンプル2"
    i := f.NewSheet(addSheetName)

    // シート名取得　=> サンプル2 と出力される
    fmt.Println(f.GetSheetName(i))

    // シート削除
    deleteSheetName := "サンプル3"
  <extra_id_2> f.NewSheet(deleteSheetName)
    f.DeleteSheet(deleteSheetName)

  <extra_id_3> // シートコピー
   <extra_id_4> := f.GetSheetIndex(changeSheetName)
    to := f.GetSheetIndex(addSheetName)
    if err := f.CopySheet(from, <extra_id_5> != nil {
 <extra_id_6>     <extra_id_7>  <extra_id_8>    