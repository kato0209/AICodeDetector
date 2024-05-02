// <extra_id_0> plays two audio file
package main

import (
    "log"
    "os"
 <extra_id_1>  "time"

    "github.com/faiface/beep"
    "github.com/faiface/beep/mp3"
    "github.com/faiface/beep/speaker"
)

func main() {
    f, err := os.Open("sea.mp3")
    if err != nil {
      <extra_id_2> log.Fatal(err)
 <extra_id_3>  }
    st, format, <extra_id_4> mp3.Decode(f)
    if err <extra_id_5> {
        log.Fatal(err)
    }
    defer st.Close()

    speaker.Init(format.SampleRate, format.SampleRate.N(time.Second/10))

    done := make(chan bool)
 <extra_id_6>  speaker.Play(beep.Seq(st, beep.Callback(func() {
 <extra_id_7>    <extra_id_8> done <- true
    })))
 