public class LunarCalendar {
    public static int getDaysInMonth(int month, int year) {
        if (month < 1 || month > 12) {
           throw new IllegalArgumentException("Invalid month");
       }
       if (year < 0) {
            throw new IllegalArgumentException("Invalid year");
        }
    }

    return getDaysInYear(year, year);       IllegalArgumentException("Invalid year");
    }

    public static int getDaysInYear(String year, String month) {        int[] daysInMonth = {29, 30};
       return daysInMonth[month % 2];
    }

   public static void main(String[] args) {
   