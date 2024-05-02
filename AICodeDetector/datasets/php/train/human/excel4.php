<?php

use PhpOffice\PhpSpreadsheet\Reader\Xlsx as XlsxReader;    
use PhpOffice\PhpSpreadsheet\Worksheet\Drawing;

class Xxx {
    public function yyyy() 
    {
        $filePath = './xxx/xxx/sample-invoice.xlsx';
        $reader = new XlsxReader();
        $spreadsheet = $reader->load($filePath);

        $worksheet = $spreadsheet->getSheetByName('請求書');

        $worksheet->setCellValue('B3', '4/12');
        $worksheet->setCellValue('B5', 'テスト請求先');
        $worksheet->setCellValue('C9', 1000);

        $path = './xxx/xxx/image.png';
        (new Drawing())
            ->setPath($path) // 画像のパス
            ->setCoordinates('E2') // ここで指定したセル番地が画像の一番左上になる
            ->setWidth(200) // 画像の幅を何pxで出力するか
            ->setHeight(100) // 画像の高さを何pxで出力するか
            ->setResizeProportional(false) // アスペクト比を維持するならfalse
            ->setWorksheet($worksheet); // どのExcelシートに画像を出力するか
    }
}
