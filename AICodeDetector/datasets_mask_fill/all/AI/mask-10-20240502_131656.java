public class DeadlockDemo {
  
    <extra_id_0> Object resource1 = new Object();
    public static Object resource2 = new Object();
  
 <extra_id_1>  public static void main(String[] args) {
 <extra_id_2>      Thread t1 = <extra_id_3> Task1());
        Thread <extra_id_4> new Thread(new Task2());
   <extra_id_5>    t1.start();
        t2.start();
    }
  
    static class Task1 implements Runnable {
  <extra_id_6>     public void run() {
      <extra_id_7>   <extra_id_8> synchronized (resource1) {
         