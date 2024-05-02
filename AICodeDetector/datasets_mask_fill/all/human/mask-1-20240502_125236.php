<?php

const NUMBER_1 = 3355;
const NUMBER_2 = 2379;

$a <extra_id_0> >= NUMBER_2 ? NUMBER_1 : NUMBER_2;
$b = NUMBER_1 < NUMBER_2 ? NUMBER_1 : NUMBER_2;

$divide = $b;

while ($divide > 0) <extra_id_1>   <extra_id_2> % $divide === 0 || $divide <extra_id_3> {
     <extra_id_4>  print "{$divide}\n";
        break;
    <extra_id_5>   $divide = $a % $b;
    $a = $b;
    $b = $divide;
}
