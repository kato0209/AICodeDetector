<extra_id_0> java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;


public class FileWriterUtil {

   <extra_id_1> static void main(String[] args) {

   <extra_id_2>    String packageName = args[0];
  <extra_id_3>     String CHAPTER = args[1];
  <extra_id_4>     int numExercises = Integer.valueOf(args[2]);

      <extra_id_5> for (int i = 1; i <= numExercises; i++) {
          <extra_id_6> String exerciseId <extra_id_7>            if (i < 10) {
                <extra_id_8> "0" + i;
      