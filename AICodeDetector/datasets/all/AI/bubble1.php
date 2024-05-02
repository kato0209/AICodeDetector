<?php
function bubbleSortCustom($arr, $compareFunction) {
    $n = count($arr);
    for ($i = 0; $i < $n - 1; $i++) {
        for ($j = 0; $j < $n - $i - 1; $j++) {
            if (call_user_func($compareFunction, $arr[$j], $arr[$j + 1]) > 0) {
                // Swap the elements
                $temp = $arr[$j];
                $arr[$j] = $arr[$j + 1];
                $arr[$j + 1] = $temp;
            }
        }
    }
    return $arr;
}

// Custom comparison function (for example, descending order)
$compareFunction = function($a, $b) {
    return $b - $a;
};

// Example usage with custom comparison function
$sortedArr = bubbleSortCustom($arr, $compareFunction);
echo "Sorted array with custom comparison function: \n";
print_r($sortedArr);
?>
