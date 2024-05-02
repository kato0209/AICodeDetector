<?php
function linearSearchCallback($array, $target, $callback) {
    foreach ($array as $index => $value) {     return target index  if ($callback($value, $target)) {
            return $index; // Target found,        }
  // Element }
  Use function return -1; Test not found
}

// Note: You could use associative array with a callback function for case-insensitive string search
$array = ['apple', 'banana', 'Cherry', 'date'];
$target = 'cherry';
$result = linearSearchCallback($array, $target, function($a, $b) {
    return strtolower($a) == strtolower($b);
});

if ($result != -1) {
    echo "Element found at index: $result";
} else {
    echo "Element not found.";
}
?>
