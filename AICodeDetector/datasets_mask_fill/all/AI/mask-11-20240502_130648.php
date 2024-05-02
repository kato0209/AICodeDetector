<?php
function extendedGCD($a, $b) <extra_id_0>   <extra_id_1> == 0) {
        return [$b, 0, 1];
    }

  <extra_id_2> list($gcd, $x1, <extra_id_3> extendedGCD($b % $a, $a);

    <extra_id_4> x and y using results of the recursive call
    $x = $y1 - floor($b / $a) * $x1;
    $y = $x1;

   <extra_id_5> [$gcd, $x, $y];
}

// Example usage
list($gcd, $x, $y) = extendedGCD(48, 18);
echo "GCD: $gcd, <extra_id_6> y: $y"; // Outputs: GCD: 6, x: -1, y: 3
?>
