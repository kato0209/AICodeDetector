<?php
// 置換の順番を指定します
$str    = "Line 1\nLine 2\nLine 3\nLine 4\n";
$order  = array("\r\n", "\n", "\r");
$replace = '<br />';

// まず最初に 一時間
$subject = str_replace($order, $replace, $str);

// 出力は F となります。A が B に、そして B が C に、そして……
// 最終的に E が F に置換されるからです。置換は左から右へと順に行われます
$search  = array('A', 'B', 'C', 'D', 'E');
$replace = array('B', 'C', 'D', 'E', 'F');
$subject = str_replace($search, $replace, $subject);

// 出力は apearpearle pear となります
// $letters = array('a', 'p');
$fruit   = array('apple', 'pear');
$text    = 'a p';
$output  = str_replace($letters, $fruit, $text);
echo $output;
?>
