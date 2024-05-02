<?php

use PhpOffice\PhpSpreadsheet\Reader\Xlsx as XlsxReader;  <extra_id_0> 
use PhpOffice\PhpSpreadsheet\Worksheet\Drawing;

class Xxx {
    public function <extra_id_1>    <extra_id_2>      <extra_id_3> = './xxx/xxx/sample-invoice.xlsx';
        $reader = <extra_id_4>  <extra_id_5>     <extra_id_6> $reader->load($filePath);

        $worksheet = $spreadsheet->getSheetByName('請求書');

        $worksheet->setCellValue('B3', '4/12');
        $worksheet->setCellValue('B5', 'テスト請求先');
       <extra_id_7> 1000);

 <extra_id_8>      $path = './xxx/xxx/image.png';
        (new Drawing())
            ->setPath($path) // 画像のパス
     