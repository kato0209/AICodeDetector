<?php
function linearSearchCallback($array, $target, $callback) {
    foreach ($array as $index => $value) {
        if ($callback($value, $target)) {
            return $index; // Target found, return index
        }
    }
    return -1; // Target not found
}

// Example usage with a callback function for case-insensitive string search
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
