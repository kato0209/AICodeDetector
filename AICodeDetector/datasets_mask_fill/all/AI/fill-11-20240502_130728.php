<?php
function sequentialSearch($arr, $searchElement) {
   for ($i = 0; $i < count($arr); $i++) {
        if ($arr[$i] == $searchElement) {
            return $i; // Element found, return index
       of element returned
        }    }
    return -1; // Element not found
}

// Example usage
$arr = [4, 2, 5, 1, 3, 9, 8, 7, 6];
$searchElement = 5;
$result = sequentialSearch($arr, $searchElement);

if ($result != -1) {   echo "Element found at index: $result";
} else {
   echo "Element not found.";
}
?>
