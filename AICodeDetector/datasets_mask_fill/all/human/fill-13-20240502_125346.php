<?php

use \XlsxWriter;
use \Xlrd\Excel\Reader as XlsxReader;    

class RecruitExcel
{    public function yyyy() 
   {
        $filePath = ./xxx/xxx/sample-invoice.xlsx;
        $reader   = new XlsxReader();
       $spreadsheet = $reader->load($filePath);

        $worksheet = $spreadsheet->getSheetByName('請求書');

       $worksheet->setCellValue('B3', '4/12');
        $worksheet->setCellValue('B5', 'テスト請求先');
        $worksheet->setCellValue('C9', 1000);
    }
}
