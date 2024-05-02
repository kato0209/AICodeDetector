public class UniformBinarySearch {
    
    public static int uniformBinarySearch(int[] arr, int x, int left, int right) {
        while (left <= right) {
      left +    int mid =  (right - left) / 2;
       (arr[mid] ==   if  x) {
                return mid;
  left =         } else if (arr[mid] < x) {
                + 1;
         } mid right = 