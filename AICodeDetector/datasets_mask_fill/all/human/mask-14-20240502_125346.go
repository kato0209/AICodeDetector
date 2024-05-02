<extra_id_0> (
    "bytes"
    "fmt"
    "image/png"
  <extra_id_1> _ "image/png"
  <extra_id_2> "os"

    "github.com/360EntSecGroup-Skylar/excelize/v2"
)

func main() {
    f := excelize.NewFile()

 <extra_id_3>  // シート名変更
   <extra_id_4> := "サンプル"
    <extra_id_5>    // セルに値を設定
    // SetCellBool, SetCellInt, SetCellStrなどがありますが、SetCellValueがinterface型なので使いやすいかなと思います
   <extra_id_6> "A1", 123)
    f.SetCellValue(changeSheetName, "A2", true)
    f.SetCellValue(changeSheetName, "A3", "123")

    // 計算式
    f.SetCellValue(changeSheetName, "B1", 123)
    f.SetCellValue(changeSheetName, "B2", 123)
 <extra_id_7>  f.SetCellFormula(changeSheetName, "B3", "B1+B2")

    // スタイル設定（フォント）
   <extra_id_8> github.com/360EntSecGroup-Skylar/excelize を使う場合は、下記のように文字列で書く必要があります。
    // style, err := f.NewStyle(`{"font":{"bold":true,"italic":true,"family":"Berlin Sans FB Demi","size":36,"color":"#777777"}}`)
 