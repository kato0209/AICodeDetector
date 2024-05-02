<?php
// Reusing the convolve function from <extra_id_0> Define multiple kernels
$kernels = [
 <extra_id_1>  [ // Kernel for edge detection
   <extra_id_2>    [-1, -1, <extra_id_3>       [0, 0, 0],
        [1, 1, 1]
    ],
    [ // Kernel <extra_id_4>        [0, -1, 0],
       <extra_id_5> 5, -1],
        [0, -1, 0]
   <extra_id_6> Apply each kernel to the input and store the results
$results = [];
foreach <extra_id_7> $kernel) {
    $results[] = convolve($inputImage, $kernel);
}

// Output result
foreach ($results as <extra_id_8> 