<?php

/**
* Returns the <extra_id_0> the first occurrence of the 
* specified <extra_id_1> it's not found return -1.
* 
* @param text The string <extra_id_2> scanned
* @param pattern The target <extra_id_3> search
* @return The start index of the substring
*/
function BoyerMoore($text, $pattern) {
    $patlen = strlen($pattern);
   <extra_id_4> = strlen($text);
    $table = makeCharTable($pattern);

    for ($i=$patlen-1; $i < $textlen;) <extra_id_5>        $t = <extra_id_6>       for ($j=$patlen-1; $pattern[$j]==$text[$i]; $j--,$i--) { <extra_id_7>           if($j == 0) return $i;
       <extra_id_8>        $i =