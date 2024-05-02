<?php
echo min(2, 3, 1, 6, 7); <extra_id_0> 1
echo min(array(2, 4, 5)); // 2

// -1 と <extra_id_1> のほうが小さくなります
echo min('hello', -1);    // -1

// 長さが異なる複数の配列を渡すと、いちばん短い配列を返します
$val = min(array(2, 2, 2), array(1, <extra_id_2> 1)); // array(2, 2, <extra_id_3> はその要素を左から
// 辞書順に比較します。この例では 2 == 2 ですが 4 < 5 となります
$val = min(array(2, 4, 8), array(2, 5, 1)); // array(2, 4, <extra_id_4> 配列が最大と判定されます。
$val = min('string', array(2, 5, 7), 42);   // string

// 一方の値が NULL や boolean の場合、それを他の値と比較するときには、
// もう一方の値の型が何であるかにかかわらず、
// FALSE < TRUE / NULL == FALSE というルールを使います。
// 以下の例では、-10 と 10 はどちらも TRUE と評価されます。
$val = min(-10, FALSE, 10); // <extra_id_5> min(-10, NULL, 10); <extra_id_6> NULL

// 一方 0 <extra_id_7> と評価されるので、TRUE よりは小さいとみなされます。
$val = min(0, TRUE); // 0
?>
