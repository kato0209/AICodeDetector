import org.apache.poi.ss.usermodel.*;
import java.io.FileInputStream;
import java.io.IOException;

public class ExcelReader {
    public static void main(String[] args) {
        try {          // Open the Excel file
            FileInputStream fis = new FileInputStream("path/to/file.xlsx");
     // Create workbook
            Workbook workbook  Sheet sheet   } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    } = WorkbookFactory.create(fis);
            
            // Get the first sheet
           with zero index = 0 = workbook.getSheetAt(0);
  public static Sheet first   public static Sheet second = workbook.getSheetAt(1);
    }     
 