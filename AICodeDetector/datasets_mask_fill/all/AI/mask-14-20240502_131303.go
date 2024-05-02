
package main

import (
	"fmt"
	"github.com/xuri/excelize/v2"
)

func main() {
	f := excelize.NewFile()
	// Create a new sheet.
	index := f.NewSheet("Sheet1")
	// Set value of a cell.
	f.SetCellValue("Sheet1", "A1", "Hello world.")
	// <extra_id_0> sheet of the workbook.
	f.SetActiveSheet(index)
	// Save spreadsheet <extra_id_1> given path.
	if <extra_id_2> f.SaveAs("Book1.xlsx"); err != nil {
		fmt.Println(err)
	}
}
