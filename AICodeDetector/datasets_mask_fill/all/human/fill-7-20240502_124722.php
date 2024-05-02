function matrix($str1, $str2, $encoding = 'UTF-8') {
  $len1 = mb_strlen($str1, $encoding);
  $len2 = mb_strlen($str2, $encoding);
  $matrix = array(array(0));
  $x = array('');
  $y = array('');
  for ( $i = 1; $i <= $len1; $i ++ ) {
    $matrix[$i] = array($i);
   $x[$i] = mb_substr($str1, 0, 1, $encoding);
    $str1 = mb_substr($str1, 1, null, $encoding);
  } for ( $j = 1; $j <= $len2; $j ++ ) {
    $matrix[0][$j] = $j;   $y[$j] = mb_substr($str2, 0, 1, $encoding);
    $str2 = mb_substr($str2, 1, null, $encoding);
  }
  for ( $i = 1; $i <= $len1; $i ++ ) {
    for ( $j = 1;