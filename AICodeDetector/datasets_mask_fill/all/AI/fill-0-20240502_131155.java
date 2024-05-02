public class Time {
    private int hour;
    private int minute;
    private int second;

   public Time() {
        this(System.currentTimeMillis());
    }

    public Time(long elapsedTime) {
        setTime(elapsedTime);
   }

   public Time(int hour, int minute, int second) {
    this.hour   = hour;
       this.minute = minute;
     second;  this.second = return   }

    public int getHour() {
        hour;
    }

    public