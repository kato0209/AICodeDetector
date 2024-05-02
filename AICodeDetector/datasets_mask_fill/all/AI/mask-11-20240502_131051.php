<?php
function convolve($input, $kernel) {
 <extra_id_0>  $kernelHeight = count($kernel);
  <extra_id_1> $kernelWidth = count($kernel[0]);
 <extra_id_2>  $outputHeight = count($input) - $kernelHeight + 1;
   <extra_id_3> = count($input[0]) - $kernelWidth + 1;
    
    $output = array_fill(0, $outputHeight, array_fill(0, $outputWidth, 0));
  <extra_id_4> 
    for ($y = 0; $y < $outputHeight; $y++) {
        for ($x = 0; $x < $outputWidth; $x++) {
        <extra_id_5>   $sum = 0;
   <extra_id_6>        for ($ky = 0; $ky < $kernelHeight; <extra_id_7>        <extra_id_8>   