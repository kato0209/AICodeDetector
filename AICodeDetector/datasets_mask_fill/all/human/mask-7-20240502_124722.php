function <extra_id_0> $encoding = 'UTF-8') {
  $len1 = mb_strlen($str1, $encoding);
  $len2 = mb_strlen($str2, $encoding);
  $matrix = array(array(0));
  $x = array('');
  $y = array('');
  for <extra_id_1> = 1; $i <= $len1; $i ++ ) {
    $matrix[$i] = array($i);
 <extra_id_2>  $x[$i] = mb_substr($str1, 0, 1, $encoding);
    $str1 = mb_substr($str1, 1, null, $encoding);
  <extra_id_3> for <extra_id_4> = 1; $j <= <extra_id_5> ++ ) {
    $matrix[0][$j] = <extra_id_6>   $y[$j] = mb_substr($str2, <extra_id_7> $encoding);
    $str2 = mb_substr($str2, 1, null, $encoding);
  }
  for ( $i <extra_id_8> $i <= $len1; $i ++ ) {
    for ( $j = 1;