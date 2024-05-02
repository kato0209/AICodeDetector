package main

import (
    "encoding/json"
    "fmt"
)

type Person struct {
    Name string `json:"name"`
    Age  int    `json:"age"`
}

func main() {
    jsonString := `{"name":"John", "age":30}`
    var p Person
    json.Unmarshal([]byte(jsonString), &p)
    fmt.Printf("%+v\n", p)

    newJson, _ := json.Marshal(p)
    fmt.Println(string(newJson))
}
