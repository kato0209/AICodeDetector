import java.util.HashSet;
import java.util.Set;

public class DocumentSimilarity {
    public <extra_id_0> jaccardSimilarity(String doc1, String doc2) {
        Set<String> set1 = new HashSet<>();
        Set<String> set2 = new HashSet<>();

 <extra_id_1>      for (String word : doc1.split(" ")) {
      <extra_id_2>     set1.add(word);
        }

     <extra_id_3>  for (String word <extra_id_4> ")) {
   <extra_id_5>        set2.add(word);
       <extra_id_6>   <extra_id_7>    Set<String> union = new HashSet<>(set1);
     <extra_id_8> 