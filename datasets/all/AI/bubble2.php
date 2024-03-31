<?php
function optimizedBubbleSort($arr) {
    $n = count($arr);
    $swapped = true;
    for ($i = 0; $i < $n - 1 && $swapped; $i++) {
        $swapped = false;
        for ($j = 0; $j < $n - $i - 1; $j++) {
            if ($arr[$j] > $arr[$j + 1]) {
                // Swap the elements
                $temp = $arr[$j];
                $arr[$j] = $arr[$j + 1];
                $arr[$j + 1] = $temp;
                $swapped = true;
            }
        }
    }
    return $arr;
}

// Example usage remains the same
$sortedArr = optimizedBubbleSort($arr);
echo "Optimized sorted array: \n";
print_r($sortedArr);
?>
