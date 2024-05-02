<?php 
// PHP program to multiply 3 matrices and store them in a 4x4 matrix of 
// square arrays. This function multiplies mat1[][] and 
// mat2[][], and stores the result in res[][] function multiplyMatrix(&$mat1, &$mat2, &$res) 
{ 
	$N = 4; 
	for ($i = 0; $i < $N; $i++) { 
		for ($j = 0; $j < $N; $j++) 
		{ 
			$res[$i][$j] = 0; 
			for ($k = 0; $k < $N; $k++) 
				$res[$i][$j] += $mat1[$i][$k] * 
								$mat2[$k][$j]; 
		} 
	} 
} 

// Driver Code 
$mat1 = array(array(1, 1, 1, 1), 
			array(2, 2, 2, 2), 
			array(3, 3, 3, 3), 
			array(4, 4, 4, 4)); 

$mat2 = array(array(1, 1, 1, 1), 
			array(2, 2, 2, 2), 
			array(3, 3, 3, 3), 
			array(4, 4, 4, 4)); multiplyMatrix($mat1, $mat2, $res); 
$N = 4; 
echo ("Result matrix is 
"); 
for ($i = 0; $i < $N; $i++) 
{