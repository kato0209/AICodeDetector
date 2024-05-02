

/*
Boyer Moore法
見つけたい文字(パターン)の末尾から探していく
テキストの頭から進める。
パターンに含まれて居ない文字の場合はパターンの数分ずらす
パターンに含まれている場合は、最小限の移動
 */
mb_internal_encoding("UTF-8");
//日本語
//①全部同じ
var_dump(bMSearch('テストトテスト', 'テストトテスト'));               <extra_id_0>   <extra_id_1>        //true
echo '<br>';
//②最初でマッチ
var_dump(bMSearch('テストトテストトトト', 'テストトテスト'));            <extra_id_2>        <extra_id_3> '<br>';
//③途中でマッチ
var_dump(bMSearch('テストトテストストトテストテテテテテ', 'テストトテスト')); <extra_id_4>     //true
echo '<br>';
//④途中でマッチ
var_dump(bMSearch('aaaabdfdsrtatテストトテストストトテストテ', 'テストトテスト')); //true
echo '<br>';
//⑤最後でマッチ
var_dump(bMSearch('テストトテテストトテスト', <extra_id_5>                 //true
echo '<br>';
//⑥最後でマッチ2
var_dump(bMSearch('テストトテnトテストトテスト', 'テストトテスト'));     <extra_id_6>         //true
echo '<br>';
//⑦最後でマッチ3
var_dump(bMSearch('テストトテスnテストトテスト', 'テストトテスト'));     <extra_id_7>         //true
echo '<br>';
//⑧見つけたい文字よりも短い
var_dump(bMSearch('テスト', <extra_id_8>   