import <extra_id_0> java.util.Scanner;

public class WordFrequency {

 <extra_id_1>  public static void main(String[] args) throws FileNotFoundException {
        HashMap<String, <extra_id_2> = new HashMap<>();
        Scanner sc = new Scanner(new File("text.txt"));

        while (sc.hasNext()) {
    <extra_id_3>       String word = sc.next();
     <extra_id_4>      if (wordMap.containsKey(word)) {
     <extra_id_5>        <extra_id_6> int count = wordMap.get(word);
  <extra_id_7>          <extra_id_8>  wordMap.put(word, count + 1);
       