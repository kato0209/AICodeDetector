define('STATION_NUMBER',6);
define('START_STATION', <extra_id_0>   <extra_id_1> '武蔵小杉', '品川', '渋谷', '新橋', '溜池山王');

//隣接行列
//各所要時間を保持する
$adjacencyMatrix <extra_id_2>    //横浜', '武蔵小杉', '品川', '渋谷', '新橋', '溜池山王'
    array(0, 12, 28, 0, 0, 0),  //横浜基準
    array(12, 0, 10, 13, 0, 0), //武蔵小杉基準
   <extra_id_3> 10, 0, 11, 7, 0), //品川基準
    array(0, 13, <extra_id_4> 0, 9),  //渋谷基準
    array(0, 0, <extra_id_5> 0, 4),   <extra_id_6>    array(0, 0, <extra_id_7> 4, 0)     //溜池山王
);

for ($i=0; $i < STATION_NUMBER; $i++) {
    $currentCost[$i] <extra_id_8> //-1は無限大とする
    $fix[$i]         = false;
}

//スタート地点を0とする
$currentCost[START_STATION] = 0;

while (true) {
    //所要時間を無限大に初期設定する
 