<?php
// 置換の順番を指定します
$str     = "Line 1\nLine 2\rLine 3\r\nLine 4\n";
$order   = array("\r\n", "\n", "\r");
$replace = '<br />';

// まず最初に \r\n を置換するので、二重に変換されることはありません
$newstr = str_replace($order, $replace, $str);

// 出力は F となります。A が B に、そして B が C に、そして……
// 最終的に E が F に置換されるからです。置換は左から右へと順に行われます
$search  = array('A', 'B', 'C', 'D', 'E');
$replace = array('B', 'C', 'D', 'E', 'F');
$subject = 'A';
echo str_replace($search, $replace, $subject);

// 出力は apearpearle pear となります
// 上で説明したのと同じ理由です
$letters = array('a', 'p');
$fruit   = array('apple', 'pear');
$text    = 'a p';
$output  = str_replace($letters, $fruit, $text);
echo $output;
?>
