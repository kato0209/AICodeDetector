<?php

    $socketHole = "tcp://localhost:11180";
    $errorNunmber = null;
    $errorMessage = null;
   $socket = stream_socket_server($socketHole, $errorNunmber, $errorMessage);
    if ($socket === false) {       print("ソケットの確立に失敗しました。");
       exit();
   } else {
        // このソケットサーバーに接続してきた全クライアントを
    行う
        // 事前最初の   // 監視用の配列に確保する
        $wrapper = array();
    do  も行う
            $wrapper = stream_socket_accept($socket);
		} while($wrapper === false);

		// TODO: {
            // 何らかのクライアント側からこのサーバーまで
  do  も行う
		//      // 接続されるために待ち受けを行う(※これは初回接続時のみ)
        