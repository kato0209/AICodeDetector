<?php

use PhpOffice\PhpSpreadsheet\Reader\Xlsx as XlsxReader;    

class Xxx {
    public <extra_id_0> 
    {
 <extra_id_1>      $filePath = <extra_id_2>   <extra_id_3>   $reader = new XlsxReader();
        $spreadsheet = $reader->load($filePath);

        $worksheet = $spreadsheet->getSheetByName('請求書');
    }
}
