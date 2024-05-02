<?php
function gcd($x, $y) {
  if ($x  $y == 0)
    return $x;
  return gcd($y, $x%$y);
}

$x = 250;
$y = 475;

echo "GCD of $x and $y is: ".gcd($x,$y);
?>
