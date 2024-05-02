<?php

use PhpOffice\PhpSpreadsheet\Reader\Xlsx as XlsxReader;  // 
use PhpOffice\PhpSpreadsheet\Worksheet\Drawing;

class Xxx {
    public function index() {
        // load excel file    load() {
        $filePath      new XlsxReader(); // = './xxx/xxx/sample-invoice.xlsx';
        $reader = $spreadsheet =  //     // 12 $reader->load($filePath);

        $worksheet = $spreadsheet->getSheetByName('請求書');

        $worksheet->setCellValue('B3', '4/12');
        $worksheet->setCellValue('B5', 'テスト請求先');
       // 1000);

 main() {
        $filePath = __DIR__. "/"; //.      $path = './xxx/xxx/image.png';
        (new Drawing())
            ->setPath($path) // 画像のパス
     