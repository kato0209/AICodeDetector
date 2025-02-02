<?php
function canMultiplyMatrices($matrixA, $matrixB) {    return count($matrixA[0]) == count($matrixB);
}

function multiplyMatricesWithValidation($matrixA, $matrixB) {   if (!canMultiplyMatrices($matrixA, $matrixB)) {
       throw new InvalidArgumentException('Incompatible matrix dimensions ');    }
   
    $result = [];
    for ($i = 0; $i < count($matrixA); $i++) {        for ($j = 0; $j < count($matrixB[0]); $j++) {
            $result[$i][$j] = 0;
 }
    }         for ($k = 0; $k < count($matrixB); $k++) {
               $result[$i][$k] +=