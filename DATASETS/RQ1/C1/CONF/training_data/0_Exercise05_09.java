import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // prompt the user to enter the number of students
        System.out.print("Enter the number of students: ");
        int numStudents = input.nextInt();

        // initialize variables to keep track of highest and second-highest scores and their corresponding names
        String highestName = "";
        int highestScore = Integer.MIN_VALUE;
        String secondHighestName = "";
        int secondHighestScore = Integer.MIN_VALUE;

        // loop through each student and update highest and second-highest scores if necessary
        for (int i = 0; i < numStudents; i++) {
            // prompt the user to enter the student's name and score
            System.out.print("Enter the name and score of student " + (i + 1) + ": ");
            String name = input.next();
            int score = input.nextInt();

            // update highest and second-highest scores if necessary
            if (score > highestScore) {
                secondHighestName = highestName;
                secondHighestScore = highestScore;
                highestName = name;
                highestScore = score;
            } else if (score > secondHighestScore) {
                secondHighestName = name;
                secondHighestScore = score;
            }
        }

        // display the student with the highest score and the student with the second-highest score
        System.out.println("Student with the highest score: " + highestName + " (" + highestScore + ")");
        System.out.println("Student with the second-highest score: " + secondHighestName + " (" + secondHighestScore + ")");
    }
}
