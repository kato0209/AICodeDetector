<?php 
// PHP program to <extra_id_0> 
// square <extra_id_1> This function multiplies mat1[][] and 
// mat2[][], and stores the result in res[][] <extra_id_2> &$mat2, &$res) 
{ 
	$N = 4; 
	for ($i = 0; $i < $N; $i++) <extra_id_3> ($j = 0; <extra_id_4> $N; $j++) 
		{ 
			$res[$i][$j] = 0; 
			for ($k = 0; $k <extra_id_5> $k++) 
				$res[$i][$j] += $mat1[$i][$k] * 
								$mat2[$k][$j]; 
		} 
	} 
} 

// Driver Code 
$mat1 = array(array(1, 1, 1, 1), 
			array(2, 2, <extra_id_6> 
			array(3, 3, 3, 3), 
			array(4, 4, 4, 4)); 

$mat2 = array(array(1, 1, 1, 1), 
			array(2, 2, 2, <extra_id_7> 3, 3, 3), 
			array(4, 4, 4, 4)); <extra_id_8> $res); 
$N = 4; 
echo ("Result matrix is 
"); 
for ($i = 0; $i < $N; $i++) 
{