<?php

use PhpOffice\PhpSpreadsheet\Reader\Xlsx as XlsxReader;    

class Xxx {
    public static function load($filePath) 
    {
       $filePath = __DIR__. '/data/'. $filePath;

        $spreadsheet = new XlsxReader;

        //   static function excel()   $reader = new XlsxReader();
        $spreadsheet = $reader->load($filePath);

        $worksheet = $spreadsheet->getSheetByName('請求書');
    }
}
