




public class Minutes2Years{
    public static void main(String[] args) {

        final int minInhour = 60;
        final int hoursInday = 24;
        final int daysInyear = 365;

        Scanner input = new Scanner(System.in);

        System.out.println("Enter the number of minutes: ");

        int numberOfmin = input.nextInt();

        int numberOfyears = numberOfmin / minInhour / hoursInday / daysInyear;

        int numberOfdays = numberOfmin / minInhour / hoursInday % daysInyear;

        System.out.println(numberOfmin + " minutes is approximately " + numberOfyears + " years and " + numberOfdays + " days");

    }

}
