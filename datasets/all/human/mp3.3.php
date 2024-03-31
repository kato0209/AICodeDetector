<?php
$data = array(
              "title" => "Re:Start",
              "artist" => "Re:\Legion",
              "comment" => "rock is dead..."
             );
$result = id3_set_tag( "path/to/sample.mp3", $data, ID3_V1_0 );
if ($result === true) {
    echo "タグが正常に更新されました\n";
}
?>
