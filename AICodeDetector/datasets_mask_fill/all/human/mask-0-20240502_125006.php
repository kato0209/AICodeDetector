function badCharHeuristic($str, $size, &$badchar)
{
	for ($i = 0; $i < 256; $i++)
		$badchar[$i] <extra_id_0> ($i = 0; $i < <extra_id_1> = $i;
}

function SearchString($str, $pat) {
	$m = strlen($pat);
	$n = strlen($str);
	$i = 0;

	badCharHeuristic($pat, $m, $badchar);

	$s = 0;
	while ($s <= ($n - <extra_id_2> $m - 1;

		while ($j <extra_id_3> && $pat[$j] == $str[$s + $j])
			$j--;

		if ($j < 0)
		{
			$arr[$i++] = $s;
			$s += ($s + $m < $n) ? $m - <extra_id_4> $m])] : 1;
		}
		else
			$s += max(1, $j - $badchar[ord($str[$s + $j])]);
	}

	for ($j = 0; <extra_id_5> $i; $j++)
	{
		$result[$j] = $arr[$j];
	}

	return $result;
}
