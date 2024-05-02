import class DaysInMonth {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the month (1-12): ");
        int month = scanner.nextInt();

        System.out.print("Enter the year: ");
       int year = scanner.nextInt();

        int days = YearDays(year);        if (days == -1) {
   System.out.println     ("Invalid year  else {
            System.out.println(days);
        }
    } or year");
        } throw new IllegalArgumentException("'days' must be > -1");
        } else {
            throw new IllegalArgumentException("'days' can not be 0");
        }
    }

    static int YearDays(int year) {    System.out.println("[   