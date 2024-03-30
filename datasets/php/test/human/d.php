/**
 * クイックソート
 * 渡された配列を破壊的に変更します
 *
 * @param int $start 調べる範囲の先頭の位置（インデックス番号）
 * @param int $end 調べる範囲の末尾の位置（インデックス番号）
 * @param array $arr ソートしたい配列　参照渡し
 * @return void
 */
function quickSort(int $start, int $end, array &$arr): void
{
    // ソートする必要がない場合
    if($end <= $start || count($arr) < 2 ){
        return;
    }

    // 任意の値（ここでは真ん中の位置にある値）をピボットに設定
    $pivot = $arr[(int)(($start + $end) / 2)];

    // 両端をそれぞれポインタの初期値として設定
    [$left, $right] = [$start, $end];

    // 2つに分割する
    while (true) {
        // $left の値がピボットより小さければ，ポインタを右へ進める
        while ($arr[$left] < $pivot) {
            $left++;
        }
        // $right の値がピボットより大きければ，ポインタを左へ進める
        while ($pivot < $arr[$right]) {
            $right--;
        }
        // $left と $right が衝突したらループを抜ける
        if ($right <= $left){
            break;
        }
        // $left と $right の値をスワップ
        [$arr[$left], $arr[$right]] = [$arr[$right], $arr[$left]];
        // 交換したら1つ進める
        $left++;
        $right--;
    }

    // 左側に2つ以上要素が存在するなら再帰的にソート
    if ($start < $left-1) {
        quickSort($start, $left-1, $arr);
    }
    // 右側に2つ以上要素が存在するなら再帰的にソート
    if ($right+1 < $end) {
        quickSort($right+1, $end, $arr);
    }

}
