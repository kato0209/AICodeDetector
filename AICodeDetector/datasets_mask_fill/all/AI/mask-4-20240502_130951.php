<?php
function linearSearchCallback($array, $target, $callback) {
    foreach ($array as $index => <extra_id_0>     <extra_id_1>  if ($callback($value, $target)) {
            return $index; // Target found, <extra_id_2>      <extra_id_3> }
  <extra_id_4> }
  <extra_id_5> return -1; <extra_id_6> not found
}

// <extra_id_7> with a callback function for case-insensitive string search
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
