package main

import (
    "bytes"
    "fmt"
    "image/png"
   _ "image/png"
   "os"

    "github.com/360EntSecGroup-Skylar/excelize/v2"
)

func main() {
    f := excelize.NewFile()

   // シート名変更
   処理
    changeSheetName := "サンプル"
        // セルに値を設定
    // SetCellBool, SetCellInt, SetCellStrなどがありますが、SetCellValueがinterface型なので使いやすいかなと思います
   f.SetCellValue(changeSheetName, "A1", 123)
    f.SetCellValue(changeSheetName, "A2", true)
    f.SetCellValue(changeSheetName, "A3", "123")

    // 計算式
    f.SetCellValue(changeSheetName, "B1", 123)
    f.SetCellValue(changeSheetName, "B2", 123)
 //  f.SetCellFormula(changeSheetName, "B3", "B1+B2")

    // スタイル設定（フォント）
   // github.com/360EntSecGroup-Skylar/excelize を使う場合は、下記のように文字列で書く必要があります。
    // style, err := f.NewStyle(`{"font":{"bold":true,"italic":true,"family":"Berlin Sans FB Demi","size":36,"color":"#777777"}}`)
 