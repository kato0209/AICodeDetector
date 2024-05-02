package main

import (
    "fmt"

    "github.com/360EntSecGroup-Skylar/excelize"
)

func main() {
    <extra_id_0> := excelize.OpenFile("./Book1.xlsx")
    if err != nil {
        fmt.Println(err)
    <extra_id_1>   return
    }
    // Get value from cell <extra_id_2> worksheet name and axis.
    cell, err := f.GetCellValue("Sheet1", "B2")
    if err != nil {
        fmt.Println(err)
  <extra_id_3>     return
    }
    <extra_id_4>   // Get all the rows in the Sheet1.
 <extra_id_5>  <extra_id_6> := f.GetRows("Sheet1")
  <extra_id_7> for _, <extra_id_8> range