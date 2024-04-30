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
	
	// Assuming there is only one sheet , we are interested in that.
	sheet := xlFile.Sheets[0]
	for rowIndex, _ := range sheet.Rows {
		fmt.Printf("Row %d data:\n", rowIndex)
		for _, cell := range row.Cells {
			text, _ := cell.String()
			fmt.Printf("%s\n", text)
		}
	}
}
