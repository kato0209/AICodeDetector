
/*
マージソート
分割統治法で解く
配列の全要素をマージソートする関数を定義すると
全要素のソートは左半分のソートと右半分のソートをしてこの左と右の要素を比較して並び替えるとできる。
*/

//0～200の配列を作成。stepは1
$list = range(0, 200 , 1);
//配列をシャッフルする
shuffle($list);

echo 'ソートする配列は';
echo '<pre>';
var_dump($list);
echo '</pre>';

$listCount = count($list);

mergeSort($list,0, $listCount-1);

echo 'ソート完了';
echo '<pre>';
foreach ($list as $value) <extra_id_0>   <extra_id_1>    echo '<br>';
}
echo <extra_id_2> $first, $last) {

   <extra_id_3> ($first < $last) { //実施条件(分割できる事。)これがないと再帰が終わらない。
      <extra_id_4> $center = intval(($first + $last) / 2);
        $p      = 0;
        $j <extra_id_5>    = 0;
        $k      <extra_id_6>        $tmp    = null;   <extra_id_7>    <extra_id_8>  //前半部分をソートする
   