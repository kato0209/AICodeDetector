package main

import "fmt"

type Shape interface {
    Area() float64
}

type Rectangle struct {
    Width, Height float64
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

func main() {
    var s Shape = Rectangle{Width: 3, Height: 4}
    fmt.Println("Area:", s.Area())
}
