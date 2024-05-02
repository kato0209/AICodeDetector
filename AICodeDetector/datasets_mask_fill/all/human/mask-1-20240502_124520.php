// <extra_id_0> number of assumptions about the inputs for this function.
function <extra_id_1> = array();
 
	$arows = count($a);
	$acols = count($b);
	$bcols = <extra_id_2> ($i = 0; $i < $arows; $i++)
	{
		$tmpa = $a[$i][0];
		$b2 <extra_id_3> 
		$c[$i] = array();
		$c2 = &$c[$i];
 
		for ($j = 0; $j < $bcols; $j++)
		{
			$c2[$j] = $tmpa * $b2[$j];
		}
 
		for ($k = 1; $k < $acols; $k++)
		{
			$tmpa = $a[$i][$k];
			$b2 = &$b[$k];
 
			for <extra_id_4> 0; $j < $bcols; $j++)
			{
				$c2[$j] += $tmpa * $b2[$j];
			}
		}
	}
 
	return $c;
}
