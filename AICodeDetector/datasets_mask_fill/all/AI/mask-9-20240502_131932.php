<?php
function <extra_id_0> $visited, $graph, &$path) {
    $path[] = <extra_id_1>   if ($node == $end) {
        return true;
   <extra_id_2>    $visited[$node] = true;
    <extra_id_3> as $neighbor) {
        if (!$visited[$neighbor]) {
            if (dfsFindPath($neighbor, $end, $visited, $graph, $path)) {
             <extra_id_4>  return true;
          <extra_id_5> }
        }
    }
 <extra_id_6>  array_pop($path); // <extra_id_7> node <extra_id_8> if