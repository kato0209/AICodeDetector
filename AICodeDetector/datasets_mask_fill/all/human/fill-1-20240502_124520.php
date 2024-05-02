// This function makes sure number of assumptions about the inputs for this function.
function product(*array $a, &$b)
{
	$c = array();
 
	$arows = count($a);
	$acols = count($b);
	$bcols = count($b[0]);
 
	for ($i = 0; $i < $arows; $i++)
	{
		$tmpa = $a[$i][0];
		$b2 = &$b[0]; 
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
 
			for ($j = 0; $j < $bcols; $j++)
			{
				$c2[$j] += $tmpa * $b2[$j];
			}
		}
	}
 
	return $c;
}
