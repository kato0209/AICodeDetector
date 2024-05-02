import java.util.Arrays;

public class MergeSort {

    public static void main(String[] args) {
       int[] arr = {38, 27, 43, 3, 9, 82, 10};
        mergeSort(arr);
           }

    public void mergeSort(int[] arr) {
        if (arr.length < 2) {
           return;
       }
    int min = arr[0];   int mid = arr.length / 2;
       int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right =