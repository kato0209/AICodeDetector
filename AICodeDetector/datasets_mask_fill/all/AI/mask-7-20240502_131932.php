<?php
function multiplyMatrices($matrixA, $matrixB) {
    $rowsA = count($matrixA);
    $colsA = count($matrixA[0]);
   <extra_id_0> = count($matrixB[0]);
    $result = array();

    for <extra_id_1> 0; $i < $rowsA; <extra_id_2>        for ($j = 0; <extra_id_3> $colsB; $j++) {
         <extra_id_4>  $result[$i][$j] = 0;
            <extra_id_5> = 0; $k < $colsA; $k++) {
       <extra_id_6>        $result[$i][$j] += $matrixA[$i][$k] * $matrixB[$k][$j];
      <extra_id_7>     <extra_id_8>     