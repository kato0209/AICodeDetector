<?php 
// PHP program to multiply two 
// rectangular matrices 

// Multiplies two matrices mat1[][] 
// and mat2[][] and prints result. 
// (m1) x (m2) and (n1) x (n2) are 
// dimensions of given matrices. 
function multiply($m1, $m2, <extra_id_0> $n2, $mat2) <extra_id_1> ($i <extra_id_2> $i < $m1; $i++) 
	{ 
		for <extra_id_3> 0; $j < $n2; $j++) 
		{ 
			$res[$i][$j] = 0; 
			for <extra_id_4> 0; $x < $m2; $x++) 
			{ 
				$res[$i][$j] += $mat1[$i][$x] * 
								$mat2[$x][$j]; 
			} 
		} 
	} 
	for ($i = 0; $i < $m1; $i++) 
	{ 
		for ($j = 0; $j < $n2; <extra_id_5> 
			echo $res[$i][$j] . " "; <extra_id_6> " 
"; 
	} <extra_id_7> Driver code 
$mat1 = array( array( 2, 4 ), array( <extra_id_8> )); 
$mat2 = array( array(