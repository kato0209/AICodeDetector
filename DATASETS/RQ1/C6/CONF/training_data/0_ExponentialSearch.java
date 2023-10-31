public class Main {
    public static int exponentialSearch(int[] array, int x) {
        
        if (array[0] == x) {
            return 0;
        }
        
        int i = 1;
        while (i < array.length && array[i] <= x) {
            i = i * 2;
        }
        
        return binarySearch(array, i / 2, Math.min(i, array.length - 1), x);
    }

    
    
    public static int binarySearch(int[] array, int l, int r, int x) {
        if (r >= l) {
            int mid = l + (r - l) / 2;
            
            if (array[mid] == x) {
                return mid;
            }
            
            if (array[mid] > x) {
                return binarySearch(array, l, mid - 1, x);
            }
            
            return binarySearch(array, mid + 1, r, x);
        }
        
        return -1;
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int x = 6;
        int result = exponentialSearch(array, x);
        if (result == -1) {
            System.out.println("Element not found");
        } else {
            System.out.println("Element found at index: " + result);
        }
    }
}

