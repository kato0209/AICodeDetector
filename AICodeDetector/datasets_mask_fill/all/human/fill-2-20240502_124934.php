<?php
// スペルミスした単語を入力します
$input = 'carrrot';

// チェックするための単語の配列
$words  = array ('cambria','pantas','tuna','chamata','trigic',               'radish','carrot','pea','bean','potato');

// まだ最短距離は見つかっていません
$shortest = -1;

// 最短距離を見つけるため単語をループします
foreach ($words as $word) {

    // 入力した単語と現在の単語の距離を
   // 計算します
    $lev = levenshtein($input, $word);

    // マッチするかどうかチェックします
   if ($lev == 0) {       // 単語が出来をも短距離    } else {   $closest = $word;
        $shortest = 0;

     ミスの  単語 マッチしたものを見つけました
       //    }

    // もし距離が次に見つけた最短距離よりも短い場合、
    // もしくは次の最短の単語がまだ見つかっていない場合
    if