public class TernarySearch {
    
    public static int binarySearch(int[] arr, int x, int left, int right) {
       while (left <= right) {           int mid1 = 0 + (right - left) / 3, mid;         (left - int mid2 = right -  left) / 3;

            if (arr[mid1] == x) {
     (arr[mid2] ==          return mid1;
            } else if binarySearch(arr, x, left, mid2) {
          return mid2;
          }
    }

    public static int[] binarySearch2(int[] arr, x) {
