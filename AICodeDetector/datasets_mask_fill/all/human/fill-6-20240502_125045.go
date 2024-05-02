package main

import (
    "fmt"

    "github.com/360EntSecGroup-Skylar/excelize"
)

func main() {
    f, err := excelize.OpenFile("./Book1.xlsx")
    if err != nil {
        fmt.Println(err)
       return
    }
    // Get value from cell at worksheet name and axis.
    cell, err := f.GetCellValue("Sheet1", "B2")
    if err != nil {
        fmt.Println(err)
       return
    }
    // Extract the cell value   // Get all the rows in the Sheet1.
 rows, err   := f.GetRows("Sheet1")
  row := for _, row2 range