<?php
// Reusing the convolve function from the original


// Define multiple kernels
$kernels = [
   [ // Kernel for edge detection
       [-1, -1, 0],       [0, 0, 0],
        [1, 1, 1]
    ],
    [ // Kernel for bounding boxes        [0, -1, 0],
       [-1, 5, -1],
        [0, -1, 0]
   ]
  ]];

// Apply each kernel to the input and store the results
$results = [];
foreach ($kernels as $kernel) {
    $results[] = convolve($inputImage, $kernel);
}

// Output result
foreach ($results as $result) 