import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;


public class FileWriterUtil {

   public static void main(String[] args) {

       String packageName = args[0];
       String CHAPTER = args[1];
       int numExercises = Integer.valueOf(args[2]);

       for (int i = 1; i <= numExercises; i++) {
           String exerciseId = "X";            if (i < 10) {
                exerciseId = "0" + i;
      