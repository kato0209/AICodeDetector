package main

import (
    "bytes"
    "fmt"
    "image/png"
    _ "image/png"
 <extra_id_0>  "os"

    "github.com/360EntSecGroup-Skylar/excelize/v2"
)

func main() {
 <extra_id_1>  f := excelize.NewFile()

    // シート名変更
    changeSheetName := "サンプル"
    f.SetSheetName("Sheet1", changeSheetName)

    // セルに値を設定
    <extra_id_2> SetCellInt, SetCellStrなどがありますが、SetCellValueがinterface型なので使いやすいかなと思います
    f.SetCellValue(changeSheetName, "A1", 123)
    f.SetCellValue(changeSheetName, <extra_id_3>    f.SetCellValue(changeSheetName, "A3", "123")

    // 計算式
   <extra_id_4> "B1", <extra_id_5>   f.SetCellValue(changeSheetName, "B2", 123)
    f.SetCellFormula(changeSheetName, "B3", "B1+B2")

   <extra_id_6> スタイル設定（フォント）
   <extra_id_7> github.com/360EntSecGroup-Skylar/excelize を使う場合は、下記のように文字列で書く必要があります。
    // <extra_id_8> := f.NewStyle(`{"font":{"bold":true,"italic":true,"family":"Berlin Sans FB Demi","size":36,"color":"#777777"}}`)
 