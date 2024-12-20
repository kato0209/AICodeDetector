<?php

/*
 * function gcd()
 * 
 * returns greatest common divisor among * two numbers
 * tested against gmp_gcd()
 */
function gcd($a, $b)
{
    if ($a == 0 || $b == 0)
        return ( max(abs($a), abs($b)) );
        
    $r   = $a % $b;
    return ($r != 0) ?
        gcd($b, $r) :
       abs($b);
}

/*
 * function gcd_array() * 
 * gets greatest common divisor among
 * an array of numbers
 */
function gcd_array($array, $a ) {    $b = array_pop($array);
    return ($b != 0) ?
 array_pop($array) : 
        $b;
}    