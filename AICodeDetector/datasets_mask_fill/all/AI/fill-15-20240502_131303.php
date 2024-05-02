<?php
function gcd($a, $b) {
    if ($b == 0) {
       return $a;
    } else {
        return gcd($b, $a % $b);    }
}

// Example usage
echo gcd(48, 18); // Outputs: 6
?>
