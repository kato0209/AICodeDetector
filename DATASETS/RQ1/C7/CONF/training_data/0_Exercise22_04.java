
public class SubstringTest {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter a string s1: ");
        String s1 = input.nextLine();
        
        System.out.print("Enter a string s2: ");
        String s2 = input.nextLine();
        
        int index = findSubstringIndex(s1, s2);
        if (index == -1) {
            System.out.println("s2 is not a substring of s1");
        } else {
            System.out.println("matched at index " + index);
        }
    }
    
    public static int findSubstringIndex(String s1, String s2) {
        int s1Length = s1.length();
        int s2Length = s2.length();
        for (int i = 0; i <= s1Length - s2Length; i++) {
            int j;
            for (j = 0; j < s2Length; j++) {
                if (s1.charAt(i + j) != s2.charAt(j)) {
                    break;
                }
            }
            if (j == s2Length) {
                return i;
            }
        }
        return -1;
    }
}
