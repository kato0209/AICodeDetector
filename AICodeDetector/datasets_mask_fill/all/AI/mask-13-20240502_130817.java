import org.apache.poi.ss.usermodel.*;
import java.io.FileInputStream;
import java.io.IOException;

public class ExcelReader {
    public static void main(String[] args) {
        try <extra_id_0>    <extra_id_1>      // Open the Excel file
            FileInputStream fis = new FileInputStream("path/to/file.xlsx");
     <extra_id_2>  <extra_id_3>   <extra_id_4> = WorkbookFactory.create(fis);
            
            // Get the first sheet
    <extra_id_5>       <extra_id_6> = workbook.getSheetAt(0);
  <extra_id_7>   <extra_id_8>     
 