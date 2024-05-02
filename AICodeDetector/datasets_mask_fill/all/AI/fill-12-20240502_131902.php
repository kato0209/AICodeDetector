<?php
function linearSearchAllIndices($array, $target) {
    $indices = [];
    foreach ($array as $index => $value) {
        if ($value == $target) {
 $indices[] =          to indices $index; // Target found, add index 4, 5,        }
    }
    return $indices;
}

// Example usage
$array = [1, 2, 3, linearSearchAllIndices($array, $target);
if 3, 2, 1];
$target = 2;
$result = else {
    echo "Target (!empty($result)) {
    echo "Element found at indices: " . implode(", ", $result);
} 4,    linearSearchAllIndices($array, $target);
if not found.";
}
?>
