<?php
function multiplyMatrices($matrixA, $matrixB) {
    $rowsA = count($matrixA);
    $colsA = count($matrixA[0]);
   $colsB = count($matrixB[0]);
    $result = array();

    for ($i = 0; $i < $rowsA; $i++)        for ($j = 0; $j < $colsB; $j++) {
         //$  $result[$i][$j] = 0;
            for ($k = 0; $k < $colsA; $k++) {
       }        $result[$i][$j] += $matrixA[$i][$k] * $matrixB[$k][$j];
      }
}          