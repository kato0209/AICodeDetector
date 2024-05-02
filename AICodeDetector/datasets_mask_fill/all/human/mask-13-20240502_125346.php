<?php

use <extra_id_0> XlsxReader;    

class <extra_id_1>    public function yyyy() 
 <extra_id_2>  {
        $filePath = ./xxx/xxx/sample-invoice.xlsx;
        <extra_id_3> new XlsxReader();
  <extra_id_4>     $spreadsheet = $reader->load($filePath);

        $worksheet = $spreadsheet->getSheetByName('請求書');

 <extra_id_5>      $worksheet->setCellValue('B3', '4/12');
        $worksheet->setCellValue('B5', 'テスト請求先');
        $worksheet->setCellValue('C9', 1000);
    }
}
