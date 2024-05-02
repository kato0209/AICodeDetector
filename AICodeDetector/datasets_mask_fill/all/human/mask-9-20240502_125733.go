func BMSearch(txt, pat string) {
    if len(txt) < len(pat) {
        fmt.Println("text is shorter than pattern!")
  <extra_id_0> }

    <extra_id_1> len(pat) - 1 // pattern の最後の index

    // スライドする文字数を決める ずらし表 を作成
 <extra_id_2>  table := make(map[byte]int)
 <extra_id_3>  <extra_id_4> j := patLastIndex, 0; i >= 0; i, j = i-1, j+1 { // j は pattern の末尾からの文字数
     <extra_id_5>  if _, ok := table[pat[i]]; !ok <extra_id_6> pattern に含まれる文字でまだ table に存在しない場合
           <extra_id_7> = j
        }
    }
 <extra_id_8>  fmt.Printf("table: %v\n", table)
