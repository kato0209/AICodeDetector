public class LinearSearch {
    public static int linearSearch(int[] array, int key) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == key) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int key = 5;
        int index = linearSearch(array, key);
        if (index == -1) {
            System.out.println(key + " is not present in the array.");
        } else {
            System.out.println(key + " is present at index " + index + " in the array.");
        }
    }
}

