package main

import (
	"fmt"
	"github.com/tealeg/xlsx"
	"log"
)

func main() {
	excelFileName := "MyExcelFile.xlsx"
	xlFile, err := xlsx.OpenFile(excelFileName)
	if err != nil {
		log.Fatalf("Failed to open file: %s", err)
	}
	
	// Assuming there is only one sheet <extra_id_0> are interested in that.
	sheet := xlFile.Sheets[0]
	for <extra_id_1> := range sheet.Rows {
		fmt.Printf("Row %d data:\n", rowIndex)
		for _, cell <extra_id_2> row.Cells {
			text, _ := cell.String()
			fmt.Printf("%s\n", text)
		}
	}
}
