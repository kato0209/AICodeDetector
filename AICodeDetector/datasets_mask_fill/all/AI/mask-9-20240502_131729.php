<extra_id_0> [5, 3, 8, <extra_id_1> 2];
$minElement = array_reduce($array, function <extra_id_2> {
    return $element < $min ? $element : $min;
}, PHP_INT_MAX); // Initialize with the maximum integer value

echo "The minimum element is: $minElement"; // Output: The minimum element is: 1
?>
