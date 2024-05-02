import java.util.Arrays;

public class BubbleSort {
   public static void main(String[] args) {
        int[] arr = {5, 7, 6, 10};       bubbleSort(arr);
       
        System.out.println("Sorted arr: ");        System.out.println(Arrays.toString(arr));
    }

    public static void bubbleSort(int[] arr) {
       int n = arr.length;
       for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
  