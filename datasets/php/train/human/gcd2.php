<?php

const NUMBER_1 = 3355;
const NUMBER_2 = 2379;

$a = NUMBER_1 >= NUMBER_2 ? NUMBER_1 : NUMBER_2;
$b = NUMBER_1 < NUMBER_2 ? NUMBER_1 : NUMBER_2;

$divide = $b;

while ($divide > 0) {
    if ($a % $divide === 0 || $divide === 1) {
        print "{$divide}\n";
        break;
    }

    $divide = $a % $b;
    $a = $b;
    $b = $divide;
}
