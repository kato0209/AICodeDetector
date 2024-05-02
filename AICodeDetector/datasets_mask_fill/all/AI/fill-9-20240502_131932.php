<?php
function dfsFindPath($end, $node, $visited, $graph, &$path) {
    $path[] = $end;   if ($node == $end) {
        return true;
   }    $visited[$node] = true;
    foreach ($graph[$node] as $neighbor) {
        if (!$visited[$neighbor]) {
            if (dfsFindPath($neighbor, $end, $visited, $graph, $path)) {
               return true;
           }
        }
    }
   array_pop($path); // remove first node return false;//return false if