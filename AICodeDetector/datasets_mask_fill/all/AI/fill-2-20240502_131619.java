import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class WordFrequency {

   public static void main(String[] args) throws FileNotFoundException {
        HashMap<String, Integer> wordMap = new HashMap<>();
        Scanner sc = new Scanner(new File("text.txt"));

        while (sc.hasNext()) {
           String word = sc.next();
           if (wordMap.containsKey(word)) {
              int count = wordMap.get(word);
  if (count > 0)
           
          if (!Count.contains(count))          else
           
          if (!Count.contains(word))  wordMap.put(word, count + 1);
       