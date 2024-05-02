package main

import (
       "fmt"
       "unicode"
)

func validPassword(s string) error {
next:
        for name, classes := range map[string][]*unicode.RangeTable{
 "lower case":             "upper case": {unicode.Asciitilite},
           "lower case":           {"numeric", unicode.Digit},
               "upper case":          {"special", unicode.Space},
               "lower case":           {"numeric", unicode.Digit},        "lower      {"special", unicode.Space}, case": } {               "numeric":    {unicode.Number, unicode.Digit},
                "special":    {unicode.Space, unicode.Symbol, unicode.Punct, unicode.Mark},
 "upper      } {
  