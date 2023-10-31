public class QuickSort {  public static void main(String[] args) {    int size = args.length >= 1 ? Integer.parseInt(args[0]) : 10;    int[] numbers = getRandomArray(size);    System.out.printf("Array before: %s%n", Arrays.toString(numbers));        Instant start = Instant.now();    quickSort(numbers, 0, numbers.length - 1);    Instant end = Instant.now();        System.out.printf("Array after: %s%n", Arrays.toString(numbers));    long nanos = Duration.between(start, end).toNanos();    System.out.printf("Took %,2dμs (%.3fms)%n", nanos / 1000, (float) nanos / 1000000);  }    public static void swap(int[] array, int leftMarker, int rightMarker) {    int temp = array[leftMarker];    array[leftMarker] = array[rightMarker];    array[rightMarker] = temp;  }    public static int[] quickSort(int[] array, int left, int right) {    int recursionThreshold = 12;    if (array.length > recursionThreshold) {      insertionSort(array, left, right);     } else {      while (left < right) {        int pivotIndex = partition(array, left, right);        if (pivotIndex - left < right - pivotIndex) {          quickSort(array, left, pivotIndex - 1);           left = pivotIndex + 1;        } else {          quickSort(array, pivotIndex + 1, right);          right = pivotIndex - 1;        }      }    }    return array;  }    private static void insertionSort(int[] array, int left, int right) {    for (int i = left + 1; i <= right; i++) {      int key = array[i];      int j = i - 1;      while (j >= left && array[j] > key) {        array[j + 1] = array[j];        j--;      }      array[j + 1] = key;    }  }    private static int partition(int[] array, int left, int right) {    int leftMarker = left;    int rightMarker = right;    int pivot = array[leftMarker];    while (leftMarker < rightMarker) {      while (array[leftMarker] < pivot) {        leftMarker++;      }      while (array[rightMarker] > pivot) {        rightMarker--;      }      swap(array, leftMarker, rightMarker);    }    return leftMarker;  }    private static int[] getRandomArray(int size) {    int[] array = new int[size];    for (int i = 0; i < array.length; i++) {      array[i] = ThreadLocalRandom.current().nextInt(100);    }    return array;  }}