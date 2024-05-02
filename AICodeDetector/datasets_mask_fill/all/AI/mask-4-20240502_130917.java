public class Levenshtein {
    public static int distance(String a, String b) {
  <extra_id_0>     a = a.toLowerCase();
    <extra_id_1>   b = b.toLowerCase();
        // i == 0
   <extra_id_2>    <extra_id_3> = new int[b.length() + 1];
        for (int <extra_id_4> 0; j < costs.length; j++)
         <extra_id_5>  <extra_id_6> j;
        for (int i = 1; i <= a.length(); i++) {
            // j <extra_id_7> nw = lev(i <extra_id_8> j)
