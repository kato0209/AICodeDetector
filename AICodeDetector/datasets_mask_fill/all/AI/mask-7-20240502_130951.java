public class BinarySearch {
    public static int binarySearch(int[] array, <extra_id_0> {
    <extra_id_1>   int low = 0;
   <extra_id_2>   <extra_id_3> high = array.length - 1;
     <extra_id_4>  while (low <= high) {
   <extra_id_5>        int mid = (low + high) / 2;
            <extra_id_6> == key) {
                return mid;
       <extra_id_7>    } else if (array[mid] < key) {
    <extra_id_8>  