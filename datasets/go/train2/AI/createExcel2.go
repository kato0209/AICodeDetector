package main

import (
	"github.com/tealeg/xlsx"
	"log"
)

func main() {
	var file *xlsx.File
	var sheet *xlsx.Sheet
	var row *xlsx.Row
	var cell *xlsx.Cell
	var err error

	file = xlsx.NewFile()
	sheet, err = file.AddSheet("Sheet1")
	if err != nil {
		log.Fatalf("Failed to add sheet: %s", err)
	}

	// Adding data to the first row.
	row = sheet.AddRow()
	cell = row.AddCell()
	cell.Value = "Name"
	cell = row.AddCell()
	cell.Value = "Age"

	// Adding data to the second row.
	row = sheet.AddRow()
	cell = row.AddCell()
	cell.Value = "John Doe"
	cell = row.AddCell()
	cell.Value = "30"

	err = file.Save("MyExcelFile.xlsx")
	if err != nil {
		log.Fatalf("Failed to save file: %s", err)
	}

	log.Println("Excel file created successfully.")
}
