public class QuickSortImproved {
    
    public static void quickSort(int[] list) {
        quickSort(list, 0, list.length - 1);
    }
    
    private static void quickSort(int[] list, int first, int last) {
        if (last > first) {
            int pivotIndex = partition(list, first, last);
            quickSort(list, first, pivotIndex - 1);
            quickSort(list, pivotIndex + 1, last);
        }
    }
    
    private static int partition(int[] list, int first, int last) {
        int pivotIndex = medianOfThree(list, first, last);
        int pivotValue = list[pivotIndex];
        int left = first + 1;
        int right = last;
        while (true) {
            while (left <= right && list[left] <= pivotValue) {
                left++;
            }
            while (left <= right && list[right] >= pivotValue) {
                right--;
            }
            if (right < left) {
                break;
            }
            int temp = list[left];
            list[left] = list[right];
            list[right] = temp;
        }
        int temp = list[first];
        list[first] = list[right];
        list[right] = temp;
        return right;
    }
    
    private static int medianOfThree(int[] list, int first, int last) {
        int mid = (first + last) / 2;
        if (list[first] > list[mid]) {
            int temp = list[first];
            list[first] = list[mid];
            list[mid] = temp;
        }
        if (list[mid] > list[last]) {
            int temp = list[mid];
            list[mid] = list[last];
            list[last] = temp;
        }
        if (list[first] > list[mid]) {
            int temp = list[first];
            list[first] = list[mid];
            list[mid] = temp;
        }
        return mid;
    }
    
    public static void main(String[] args) {
        int[] list = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};
        quickSort(list);
        System.out.println(Arrays.toString(list));
    }
}
