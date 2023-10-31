



public class CharactherSorter{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = in.nextLine().trim();

        System.out.print("Sorted result -> ");
        System.out.print(sort(str));

        in.close();
    }

    
    public static String sort(String s) {
        char[] chars = s.toCharArray();
        boolean notSorted = true;
        for (int i = 1; i < chars.length && notSorted; i++) {
            notSorted = false; 
            for (int j = 0; j < chars.length - i; j++) {
                if (chars[j] > chars[j + 1]) {
                    chars = swap(j, j + 1, chars);
                    notSorted = true;
                }
            }
        }
        return Arrays.toString(chars);

    }

    
    static char[] swap(int idx1, int idx2, char[] arr) {
        char temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;

        return arr;

    }
}
