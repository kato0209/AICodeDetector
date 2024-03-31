<?php
function convolveWithPaddingAndStride($input, $kernel, $padding = 0, $stride = 1) {
    $kernelHeight = count($kernel);
    $kernelWidth = count($kernel[0]);
    $inputHeight = count($input);
    $inputWidth = count($input[0]);
    
    // Adjust input dimensions based on padding
    $paddedHeight = $inputHeight + 2 * $padding;
    $paddedWidth = $inputWidth + 2 * $padding;
    $paddedInput = array_fill(0, $paddedHeight, array_fill(0, $paddedWidth, 0));
    
    // Copy input into padded input
    for ($y = 0; $y < $inputHeight; $y++) {
        for ($x = 0; $x < $inputWidth; $x++) {
            $paddedInput[$y + $padding][$x + $padding] = $input[$y][$x];
        }
    }
    
    // Calculate output dimensions
    $outputHeight = floor(($paddedHeight - $kernelHeight) / $stride) + 1;
    $outputWidth = floor(($paddedWidth - $kernelWidth) / $stride) + 1;
    
    $output = array_fill(0, $outputHeight, array_fill(0, $outputWidth, 0));
    
    for ($y = 0; $y < $outputHeight; $y++) {
        for ($x = 0; $x < $outputWidth; $x++) {
            $sum = 0;
            for ($ky = 0; $ky < $kernelHeight; $ky++) {
                for ($kx = 0; $kx < $kernelWidth; $kx++) {
                    $sum += $paddedInput[$y * $stride + $ky][$x * $stride + $kx] * $kernel[$ky][$kx];
                }
            }
            $output[$y][$x] = $sum;
        }
    }
    
    return $output;
}

// Using the same example input and kernel as before, with padding and stride
$output = convolveWithPaddingAndStride($inputImage, $kernel, 1, 2);

// Output result
foreach ($output as $row) {
    foreach ($row as $value) {
        echo "$value ";
    }
    echo "\n";
}
?>
