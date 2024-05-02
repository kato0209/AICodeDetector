package main

import (
      <extra_id_0> "fmt"
      <extra_id_1> "unicode"
)

func validPassword(s string) error {
next:
        for name, classes := range map[string][]*unicode.RangeTable{
 <extra_id_2>   <extra_id_3>          "upper case": <extra_id_4>        <extra_id_5>      <extra_id_6> case": <extra_id_7>               "numeric":    {unicode.Number, unicode.Digit},
                "special":    {unicode.Space, unicode.Symbol, unicode.Punct, unicode.Mark},
 <extra_id_8>      } {
  