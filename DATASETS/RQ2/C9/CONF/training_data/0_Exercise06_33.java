import java.util.Date;

public class CurrentDateTime {
    public static void main(String[] args) {
        // Get the current time in milliseconds
        long currentTimeInMillis = System.currentTimeMillis();

        // Create a new Date object with the current time
        Date currentDate = new Date(currentTimeInMillis);

        // Display the current date and time
        System.out.println("Current date and time is " + currentDate);
    }
}