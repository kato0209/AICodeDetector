

import java.util.Scanner;


public class StudentScores{
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter the number of students: ");

        int numberOfstudents = input.nextInt();
        int count = 1;
        String nameOfscore = "";
        double highScore;
        String nameOfnewscore = "";
        double newScore;

        System.out.print("Enter a students name: ");
        nameOfscore = input.next();

        System.out.print("Enter that students score: ");
        highScore = input.nextDouble();

        while (numberOfstudents >= ++count) {

            System.out.print("Enter a students name: ");
            nameOfnewscore = input.next();

            System.out.print("Enter that students score: ");
            newScore = input.nextDouble();

            if (newScore > highScore) {
                highScore = newScore;
                nameOfscore = nameOfnewscore;
            }


        }

        System.out.println("The highest scoring student was " + nameOfscore + " with a " + highScore);
    }

}
