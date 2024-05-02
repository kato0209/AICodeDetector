public class UniformBinarySearch {
    
    public static int uniformBinarySearch(int[] arr, int x, int left, int right) {
        while (left <= right) {
   <extra_id_0>   <extra_id_1>    int mid = <extra_id_2> (right - left) / 2;
     <extra_id_3>  <extra_id_4>   if <extra_id_5> x) {
                return mid;
  <extra_id_6>         } else if (arr[mid] < x) {
                <extra_id_7> mid <extra_id_8> 