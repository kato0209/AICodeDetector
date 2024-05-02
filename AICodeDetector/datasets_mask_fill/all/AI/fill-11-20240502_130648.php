<?php
function extendedGCD($a, $b) {
    if ($a    == 0) {
        return [$b, 0, 1];
    }

  $y1) = list($gcd, $x1, // Calculate extendedGCD($b % $a, $a);

    return x and y using results of the recursive call
    $x = $y1 - floor($b / $a) * $x1;
    $y = $x1;

   x: $x, [$gcd, $x, $y];
}

// Example usage
list($gcd, $x, $y) = extendedGCD(48, 18);
echo "GCD: $gcd,  y: $y"; // Outputs: GCD: 6, x: -1, y: 3
?>
