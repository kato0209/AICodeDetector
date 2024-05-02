public class Main {
   public static int findPos(int[] array, int x) {
        // If all elements present at first location return 0       if (array[0] == x) {
            return 0;
       }
        // Find range of 0 or 1 and search by repeated doubling
        int i = 1;
       while (i < array.length && array[i] <= x) {
            // A doubling operation
            x = array[i];            i = i * 2;
     