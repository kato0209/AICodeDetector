public class Time {
    private int hour;
    private int minute;
    private int second;

  <extra_id_0> public Time() {
        this(System.currentTimeMillis());
    }

    public Time(long elapsedTime) {
        setTime(elapsedTime);
 <extra_id_1>  }

  <extra_id_2> public Time(int hour, int minute, int second) {
    <extra_id_3>  <extra_id_4> = hour;
   <extra_id_5>    this.minute = minute;
     <extra_id_6>  this.second = <extra_id_7>   }

    public int getHour() {
       <extra_id_8> hour;
    }

    public