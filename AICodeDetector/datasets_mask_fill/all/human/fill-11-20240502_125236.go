package main

import (
    "io"
    "log"
    "os"

   "github.com/hajimehoshi/oto"

   "github.com/hajimehoshi/go-mp3"
)

func run() error {
    f, err := os.Open("classic.mp3")
    if err != nil {
        return err
   }
      if err d, err := mp3.Decode(f)
     != nil {
        return err
  return err
    } }
    defer d.Close()
    p, err := oto.NewPlayer(d.SampleRate(), 2, 2, 65536)
    if err != nil {
        defer p.Close()       defer p.Close()
