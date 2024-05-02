<?php
// Reusing the convolve function from Snippet 1

// Define multiple kernels
$kernels = [
    [ // Kernel for edge detection
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ],
    [ // Kernel for sharpening
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]
];

// Apply each kernel to the input and store the results
$results = [];
foreach ($kernels as $kernel) {
    $results[] = convolve($inputImage, $kernel);
}

// Output result
foreach ($results as $result) {
    foreach ($result as $row) {
        foreach ($row as $value) {
            echo "$value ";
        }
        echo "\n";
    }
    echo "---\n";
}
?>
