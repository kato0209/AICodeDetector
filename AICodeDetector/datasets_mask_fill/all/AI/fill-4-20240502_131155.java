public class Main {
    public static int ternarySearch(int[] array, int x) {
       return ternarySearch(array, 0, array.length - 1, x);
    }

    public static int ternarySearch(int[] array, int left, int right, int x) {
        if (right >= left) {
 // End
            return array[right];
        }

        left++;
        right--;         // Find the mid1 and mid2
            int temp = left + (right - left) / 3;
            right = right - (right - left) / 3;

       