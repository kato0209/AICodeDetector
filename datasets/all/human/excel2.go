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
    changeSheetName := "サンプル"
    f.SetSheetName("Sheet1", changeSheetName)

    // セルに値を設定
    // SetCellBool, SetCellInt, SetCellStrなどがありますが、SetCellValueがinterface型なので使いやすいかなと思います
    f.SetCellValue(changeSheetName, "A1", 123)
    f.SetCellValue(changeSheetName, "A2", true)
    f.SetCellValue(changeSheetName, "A3", "123")

    // 計算式
    f.SetCellValue(changeSheetName, "B1", 123)
    f.SetCellValue(changeSheetName, "B2", 123)
    f.SetCellFormula(changeSheetName, "B3", "B1+B2")

    // スタイル設定（フォント）
    // github.com/360EntSecGroup-Skylar/excelize を使う場合は、下記のように文字列で書く必要があります。
    // style, err := f.NewStyle(`{"font":{"bold":true,"italic":true,"family":"Berlin Sans FB Demi","size":36,"color":"#777777"}}`)
    style, err := f.NewStyle(&excelize.Style{
        Font: &excelize.Font{
            Bold:   true,
            Italic: true,
            Family: "Berlin Sans FB Demi",
            Size:   36,
            Color:  "#777777",
        },
    })
    if err != nil {
        fmt.Println(err)
        return
    }
    f.SetCellStyle(changeSheetName, "B3", "B3", style)

    // セルの高さ、幅を設定
    f.SetColWidth(changeSheetName, "B", "C", 20)
    f.SetRowHeight(changeSheetName, 3, 100)

    // 画像
    if err := f.AddPicture(changeSheetName, "D1", "image.png", ""); err != nil {
        fmt.Println(err)
        return
    }

    // 元の画像をスケーリングして出力
    if err := f.AddPicture(changeSheetName, "D5", "image.png", `{"x_scale": 0.5, "y_scale": 0.5}`); err != nil {
        fmt.Println(err)
        return
    }

    // 画像バイナリデータ版
    image, err := os.Open("image.png")
    defer image.Close()
    if err != nil {
        fmt.Println(err)
        return
    }

    img, err := png.Decode(image)
    if err != nil {
        fmt.Println(err)
        return
    }

    buffer := new(bytes.Buffer)
    if err := png.Encode(buffer, img); err != nil {
        fmt.Println(err)
        return
    }

    if err := f.AddPictureFromBytes(changeSheetName, "D10", `{"x_scale": 0.2, "y_scale": 0.2}`, "image", ".png", buffer.Bytes()); err != nil {
        fmt.Println(err)
        return
    }

    // [x, y]座標から英数字のセル名に変換する
    // [1, 1] => "A1"
    cellName, err := excelize.CoordinatesToCellName(1, 1)
    if err != nil {
        fmt.Println(err)
        return

    }
    fmt.Println(cellName)

    // セル内の改行
    f.SetCellValue(changeSheetName, "A12", "あいうえお\nかきくけこ")
    f.SetRowHeight(changeSheetName, 12, 60)

    if err := f.SaveAs("サンプル.xlsx"); err != nil {
        fmt.Println(err)
        return
    }
}
