package main

import <extra_id_0>    <extra_id_1>  "fmt"
  <extra_id_2>     "unicode"
)

func validPassword(s string) error <extra_id_3>       for name, classes := range map[string][]*unicode.RangeTable{
                "upper case": {unicode.Upper, unicode.Title},
           <extra_id_4>    "lower case": {unicode.Lower},
                "numeric":  <extra_id_5> {unicode.Number, unicode.Digit},
   <extra_id_6>         <extra_id_7>  "special":    {unicode.Space, unicode.Symbol, unicode.Punct, unicode.Mark},
     <extra_id_8>  } {
  