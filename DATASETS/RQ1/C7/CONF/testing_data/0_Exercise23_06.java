
public class OrderChecker {
    
    public static boolean ordered(int[] list) {
        return ordered(list, true);
    }
    
    public static boolean ordered(int[] list, boolean ascending) {
        if (ascending) {
            for (int i = 0; i < list.length - 1; i++) {
                if (list[i] > list[i+1]) {
                    return false;
                }
            }
        } else {
            for (int i = 0; i < list.length - 1; i++) {
                if (list[i] < list[i+1]) {
                    return false;
                }
            }
        }
        return true;
    }
    
    public static boolean ordered(double[] list) {
        return ordered(list, true);
    }
    
    public static boolean ordered(double[] list, boolean ascending) {
        if (ascending) {
            for (int i = 0; i < list.length - 1; i++) {
                if (list[i] > list[i+1]) {
                    return false;
                }
            }
        } else {
            for (int i = 0; i < list.length - 1; i++) {
                if (list[i] < list[i+1]) {
                    return false;
                }
            }
        }
        return true;
    }
    
    public static <E extends Comparable<E>> boolean ordered(E[] list) {
        return ordered(list, true);
    }
    
    public static <E extends Comparable<E>> boolean ordered(E[] list, boolean ascending) {
        if (ascending) {
            for (int i = 0; i < list.length - 1; i++) {
                if (list[i].compareTo(list[i+1]) > 0) {
                    return false;
                }
            }
        } else {
            for (int i = 0; i < list.length - 1; i++) {
                if (list[i].compareTo(list[i+1]) < 0) {
                    return false;
                }
            }
        }
        return true;
    }
    
    public static <E> boolean ordered(E[] list, Comparator<? super E> comparator) {
        return ordered(list, comparator, true);
    }
    
    public static <E> boolean ordered(E[] list, Comparator<? super E> comparator, boolean ascending) {
        if (ascending) {
            for (int i = 0; i < list.length - 1; i++) {
                if (comparator.compare(list[i], list[i+1]) > 0) {
                    return false;
                }
            }
        } else {
            for (int i = 0; i < list.length - 1; i++) {
                if (comparator.compare(list[i], list[i+1]) < 0) {
                    return false;
                }
            }
        }
        return true;
    }
}
