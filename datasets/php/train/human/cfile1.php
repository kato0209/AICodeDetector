<!DOCTYPE html>
<html>
<head>
 <title>PHPサンプル</title>
</head>
<body>
<?php
  $flg = copy('test.txt', 'test2.txt');
  if ($flg) {
    echo "コピー成功です";
  } else {
    echo "コピー失敗です";
  }
?>
</body>
</html>
