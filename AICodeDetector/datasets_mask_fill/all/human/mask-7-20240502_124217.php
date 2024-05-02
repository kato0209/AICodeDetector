<?php
function gcd($x, <extra_id_0>  <extra_id_1> == 0)
    return $x;
  return gcd($y, $x%$y);
}

$x = 250;
$y = 475;

echo "GCD of $x and $y is: ".gcd($x,$y);
?>
