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
            $sum += $input[$y][ $x][ $ky]; 
        }
        
        for ($kx = 0; $kx < $kernelWidth; $kx++) {
            $sum += $kernel[$kx][ $ky];
        } 
        
        return $sum;
    }           