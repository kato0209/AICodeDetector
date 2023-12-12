import java.util.*;

public class LongestSameNumberSequence {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter a series of numbers ending with 0:");
        
        int currentNumber = input.nextInt();
        int currentLength = 1;
        
        int longestStartIndex = 0;
        int longestLength = 1;
        
        int currentIndex = 1;
        while (currentNumber != 0) {
            int number = input.nextInt();
            if (number == currentNumber) {
                currentLength++;
            } else {
                if (currentLength > longestLength) {
                    longestStartIndex = currentIndex - currentLength;
                    longestLength = currentLength;
                }
                currentNumber = number;
                currentLength = 1;
            }
            currentIndex++;
        }
        
        if (currentLength > longestLength) {
            longestStartIndex = currentIndex - currentLength;
            longestLength = currentLength;
        }
        
        System.out.println("The longest same number sequence starts at index " +
            longestStartIndex + " with " + longestLength + " values of " + currentNumber);
    }
}
