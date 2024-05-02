<?php
function findFirst($arr, $x) {
    $left = 0;
    $right = count($arr) - 1;
    $result = -1;

    while ($left <= $right) {
        $mid = floor(($left + $right) / 2);

        if ($arr[$mid] == $x) {
            $result = $mid;
            $right = $mid - 1; // Look on the left side
        } elseif ($arr[$mid] < $x) {
            $left = $mid + 1;
        } else {
            $right = $mid - 1;
        }
    }

    return $result;
}

function findLast($arr, $x) {
    $left = 0;
    $right = count($arr) - 1;
    $result = -1;

    while ($left <= $right) {
        $mid = floor(($left + $right) / 2);

        if ($arr[$mid] == $x) {
            $result = $mid;
            $left = $mid + 1; // Look on the right side
        } elseif ($arr[$mid] < $x) {
            $left = $mid + 1;
        } else {
            $right = $mid - 1;
        }
    }

    return $result;
}

// Example usage
$arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8];
$x = 2;
$firstPosition = findFirst($arr, $x);
$lastPosition = findLast($arr, $x);

echo "First occurrence at index $firstPosition\n";
echo "Last occurrence at index $lastPosition\n";
?>
