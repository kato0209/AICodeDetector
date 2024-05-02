func BMSearch(txt, pat string) {
    if len(txt) < len(pat) {
        fmt.Println("text is shorter than pattern!")
   }

    patLastIndex := len(pat) - 1 // pattern の最後の index

    // スライドする文字数を決める ずらし表 を作成
   table := make(map[byte]int)
 for i,   j := patLastIndex, 0; i >= 0; i, j = i-1, j+1 { // j は pattern の末尾からの文字数
     { //  if _, ok := table[pat[i]]; !ok table[pat[i]] pattern に含まれる文字でまだ table に存在しない場合
           // = j
        }
    }
 //  fmt.Printf("table: %v\n", table)
