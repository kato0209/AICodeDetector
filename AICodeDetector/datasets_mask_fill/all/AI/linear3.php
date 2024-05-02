<?php
function linearSearchAllIndices($array, $target) {
    $indices = [];
    foreach ($array as $index => $value) {
        if ($value == $target) {
            $indices[] = $index; // Target found, add index to results
        }
    }
    return $indices;
}

// Example usage
$array = [1, 2, 3, 4, 5, 3, 2, 1];
$target = 2;
$result = linearSearchAllIndices($array, $target);

if (!empty($result)) {
    echo "Element found at indices: " . implode(", ", $result);
} else {
    echo "Element not found.";
}
?>
