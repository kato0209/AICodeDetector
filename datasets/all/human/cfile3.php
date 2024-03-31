<?php
try {
    $phar = new Phar('myphar.phar');
    $phar['a'] = 'hi';
    $phar->copy('a', 'b');
    echo $phar['b']; // 出力は "hi"
} catch (Exception $e) {
    // エラー処理
}

// 上のコードと同等の処理をストリームラッパーで行う例。
// エラー時には例外ではなく E_WARNINGS が発生します
copy('phar://myphar.phar/a', 'phar//myphar.phar/c');
echo file_get_contents('phar://myphar.phar/c'); // 出力は "hi"
?>
