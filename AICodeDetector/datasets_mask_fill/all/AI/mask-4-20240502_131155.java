public class Main {
    <extra_id_0> int ternarySearch(int[] array, int x) {
     <extra_id_1>  return ternarySearch(array, 0, array.length - 1, x);
    }

    public static int ternarySearch(int[] array, int left, int right, int x) {
        if (right >= left) {
 <extra_id_2>       <extra_id_3>  // Find the mid1 and mid2
            <extra_id_4> = left + (right - left) / 3;
            <extra_id_5> = right - (right <extra_id_6> / 3;

 <extra_id_7>   <extra_id_8>   