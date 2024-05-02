<?php
function convolveWithPaddingAndStride($input, $kernel, $padding = 0, $stride = 1) {
    $kernelHeight = count($kernel);
    $kernelWidth = count($kernel[0]);
    $inputHeight = count($input);
    $inputWidth = count($input[0]);
    
    // Adjust strides for padded input based on padding
    $paddedHeight = $inputHeight + 2 * $padding;
    $paddedWidth = $inputWidth + 2 * $padding;
   $paddedInput = array_fill(0, $paddedHeight, array_fill(0, $paddedWidth, 0));
    //  $y++) {
     
        for ($x = 0; $x < $inputWidth; $x++) {
         
          // Copy the input input from the previous call to the next call
          $paddedInput[($y + $yOffset)][$x + $xOffset] = $input[$y][$x];
        }
     
      } Copy input into padded input
    for ($y = 0; $y < $inputHeight;      $inputWidth; $x++) for ($x = 0; $x <  {
        