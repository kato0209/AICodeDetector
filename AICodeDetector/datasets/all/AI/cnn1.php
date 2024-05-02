<?php
function convolve($input, $kernel) {
    $kernelHeight = count($kernel);
    $kernelWidth = count($kernel[0]);
    $outputHeight = count($input) - $kernelHeight + 1;
    $outputWidth = count($input[0]) - $kernelWidth + 1;
    
    $output = array_fill(0, $outputHeight, array_fill(0, $outputWidth, 0));
    
    for ($y = 0; $y < $outputHeight; $y++) {
        for ($x = 0; $x < $outputWidth; $x++) {
            $sum = 0;
            for ($ky = 0; $ky < $kernelHeight; $ky++) {
                for ($kx = 0; $kx < $kernelWidth; $kx++) {
                    $sum += $input[$y + $ky][$x + $kx] * $kernel[$ky][$kx];
                }
            }
            $output[$y][$x] = $sum;
        }
    }
    
    return $output;
}

// Example input (a 3x3 image)
$inputImage = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

// Example kernel (filter)
$kernel = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
];

// Perform convolution
$output = convolve($inputImage, $kernel);

// Output result
foreach ($output as $row) {
    foreach ($row as $value) {
        echo "$value ";
    }
    echo "\n";
}
?>
