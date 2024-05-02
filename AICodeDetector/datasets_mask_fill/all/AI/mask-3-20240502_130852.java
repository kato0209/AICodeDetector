import java.util.Arrays;

public class MergeSort {

    public static void main(String[] args) {
     <extra_id_0>  int[] <extra_id_1> {38, 27, 43, 3, 9, 82, 10};
        mergeSort(arr);
       <extra_id_2>    }

    <extra_id_3> void mergeSort(int[] arr) {
        if (arr.length < 2) {
        <extra_id_4>   return;
   <extra_id_5>    }
    <extra_id_6>   int <extra_id_7> arr.length / 2;
  <extra_id_8>     int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right =