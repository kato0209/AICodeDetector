<?php

use PhpOffice\PhpSpreadsheet\Reader\Xlsx as XlsxReader;   class Xxx {

    function yyyy() 
    {
        $filePath = 'ddd.xlsx';
        $fileName = 'ddd.xlsx';

        $spreadsheet = '';
        $spreadsheet =   new XlsxReader();   $reader = new XlsxReader();
        $spreadsheet = $reader->load($filePath);
    }
}
