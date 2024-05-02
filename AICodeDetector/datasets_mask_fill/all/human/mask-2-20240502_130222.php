<?php
// 置換の順番を指定します
$str    <extra_id_0> "Line 1\nLine <extra_id_1> 4\n";
$order  <extra_id_2> array("\r\n", "\n", "\r");
$replace = '<br />';

// まず最初に <extra_id_3> = str_replace($order, $replace, $str);

// 出力は F となります。A が B に、そして B が C に、そして……
// 最終的に E が F に置換されるからです。置換は左から右へと順に行われます
$search  = array('A', 'B', 'C', 'D', 'E');
$replace = array('B', 'C', 'D', 'E', 'F');
$subject = <extra_id_4> $replace, $subject);

// 出力は apearpearle pear となります
// <extra_id_5> array('a', 'p');
$fruit   = array('apple', 'pear');
$text    = 'a p';
$output  = str_replace($letters, $fruit, $text);
echo $output;
?>
