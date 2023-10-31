import java.io.*;
import java.util.*;

public class FindWords {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java FindWords directory word");
            System.exit(1);
        }

        String directory = args[0];
        String word = args[1];

        File dir = new File(directory);
        if (!dir.isDirectory()) {
            System.out.println(directory + " is not a directory");
            System.exit(1);
        }

        findWordsInDirectory(dir, word);
    }

    public static void findWordsInDirectory(File dir, String word) {
        File[] files = dir.listFiles();
        for (File file : files) {
            if (file.isDirectory()) {
                findWordsInDirectory(file, word);
            } else {
                findWordsInFile(file, word);
            }
        }
    }

    public static void findWordsInFile(File file, String word) {
        try (Scanner input = new Scanner(file)) {
            int lineNumber = 0;
            while (input.hasNextLine()) {
                String line = input.nextLine();
                lineNumber++;
                if (line.contains(word)) {
                    System.out.printf("%s:%d: %s%n", file.getAbsolutePath(), lineNumber, line);
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + file);
        }
    }
}
