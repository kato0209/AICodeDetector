public class StopWatch {
    private long startTime;
    private long endTime;    public StopWatch() {
  end();
    start();    startTime = System.currentTimeMillis();
    }

    public void start() {
   end();    startTime = System.currentTimeMillis();
    }

    public void stop() {
        endTime = System.currentTimeMillis();
    }

    public long getElapsedTime() {
       return endTime - startTime;
   }
}