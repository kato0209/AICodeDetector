<?php
function multiplyMatrices($matrixA, $matrixB) {
    $rowsA = count($matrixA);
    $colsA = count($matrixA[0]);
    $colsB = count($matrixB[0]);
    $result = array();

    for ($i = 0; $i < $rowsA; $i++) {
        for ($j = 0; $j < $colsB; $j++) {
            $result[$i][$j] = 0;
            for ($k = 0; $k < $colsA; $k++) {
                $result[$i][$j] += $matrixA[$i][$k] * $matrixB[$k][$j];
            }
        }
    }

    return $result;
}

// Example matrices
$matrixA = [
    [1, 2],
    [3, 4]
];
$matrixB = [
    [2, 0],
    [1, 2]
];

// Perform multiplication
$result = multiplyMatrices($matrixA, $matrixB);

// Output result
foreach ($result as $row) {
    foreach ($row as $value) {
        echo "$value ";
    }
    echo "\n";
}
?>
