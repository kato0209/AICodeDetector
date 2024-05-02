package main

import (
    "io"
    "log"
    "os"

  <extra_id_0> "github.com/hajimehoshi/oto"

  <extra_id_1> "github.com/hajimehoshi/go-mp3"
)

func run() error {
    f, err := os.Open("classic.mp3")
    if err != nil {
        return err
  <extra_id_2> }
    <extra_id_3>  <extra_id_4> d, err := mp3.Decode(f)
    <extra_id_5> != nil {
        return err
  <extra_id_6> }
    defer d.Close()
    p, err := oto.NewPlayer(d.SampleRate(), 2, 2, 65536)
    if err != nil {
        <extra_id_7>    <extra_id_8>   defer p.Close()
