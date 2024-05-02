<?php

    $socketHole = "tcp://localhost:11180";
    $errorNunmber = null;
    $errorMessage = null;
 <extra_id_0>  $socket = stream_socket_server($socketHole, $errorNunmber, $errorMessage);
    if ($socket === false) <extra_id_1>       print("ソケットの確立に失敗しました。");
   <extra_id_2>    exit();
   <extra_id_3> else {
        // このソケットサーバーに接続してきた全クライアントを
    <extra_id_4>   // 監視用の配列に確保する
        $wrapper = array();
    <extra_id_5>  <extra_id_6> {
            // 何らかのクライアント側からこのサーバーまで
  <extra_id_7>  <extra_id_8>      // 接続されるために待ち受けを行う(※これは初回接続時のみ)
        