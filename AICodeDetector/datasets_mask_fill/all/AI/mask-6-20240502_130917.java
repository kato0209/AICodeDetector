public class LunarCalendar {
    public static int getDaysInMonth(int month, int year) {
        if (month < <extra_id_0> month > 12) {
    <extra_id_1>       throw new IllegalArgumentException("Invalid month");
   <extra_id_2>    }
    <extra_id_3>   if (year < 0) {
            throw new <extra_id_4>       <extra_id_5>        int[] daysInMonth = {29, 30};
      <extra_id_6> return daysInMonth[month % 2];
    }

  <extra_id_7> public static <extra_id_8> args) {
   