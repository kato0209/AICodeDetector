public class StopWatch {
    private long startTime;
    private <extra_id_0>    public StopWatch() {
  <extra_id_1>   <extra_id_2> startTime = System.currentTimeMillis();
    }

    public void start() {
   <extra_id_3>    startTime = System.currentTimeMillis();
    }

    public void stop() {
        endTime = System.currentTimeMillis();
    }

    <extra_id_4> getElapsedTime() {
    <extra_id_5>   return endTime - startTime;
 <extra_id_6>  }
}