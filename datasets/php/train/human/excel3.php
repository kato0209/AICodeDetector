<?php

use PhpOffice\PhpSpreadsheet\Reader\Xlsx as XlsxReader;    

class Xxx {
    public function yyyy() 
    {
        $filePath = ./xxx/xxx/sample-invoice.xlsx;
        $reader = new XlsxReader();
        $spreadsheet = $reader->load($filePath);

        $worksheet = $spreadsheet->getSheetByName('請求書');
    }
}
