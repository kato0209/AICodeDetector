<?php

$it = new AppendIterator();

// globでディレクトリ内のテキストファイルを検索
foreach(glob("dir/*.txt") as <extra_id_0> SplFileObject($filename, "r"));
}

// 新しいファイルを作成する
$file = new SplFileObject("all.txt", "w");

// 1行ずつ読み込んでデータをファイルに追加する
foreach($it as $line)
{
	$file->fwrite($line);
}
