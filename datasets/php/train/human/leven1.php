<?php
// スペルミスした単語を入力します
$input = 'carrrot';

// チェックするための単語の配列
$words  = array('apple','pineapple','banana','orange',
                'radish','carrot','pea','bean','potato');

// まだ最短距離は見つかっていません
$shortest = -1;

// 最短距離を見つけるため単語をループします
foreach ($words as $word) {

    // 入力した単語と現在の単語の距離を
    // 計算します
    $lev = levenshtein($input, $word);

    // マッチするかどうかチェックします
    if ($lev == 0) {

        // 最短な単語はこれだ (マッチした)
        $closest = $word;
        $shortest = 0;

        // ループを抜ける; マッチしたものを見つけました
        break;
    }

    // もし距離が次に見つけた最短距離よりも短い場合、
    // もしくは次の最短の単語がまだ見つかっていない場合
    if ($lev <= $shortest || $shortest < 0) {
        // 最短のマッチと最短距離をセットします
        $closest  = $word;
        $shortest = $lev;
    }
}

echo "入力した単語: $input\n";
if ($shortest == 0) {
    echo "一致するものが見つかりました: $closest\n";
} else {
    echo "もしかして: $closest\n";
}

?>
