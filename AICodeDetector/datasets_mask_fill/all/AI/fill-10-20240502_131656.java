public class DeadlockDemo {
  
    public static Object resource1 = new Object();
    public static Object resource2 = new Object();
  
   public static void main(String[] args) {
       Thread t1 = new Thread(new Task1());
        Thread t2 = new Thread(new Task2());
       t1.start();
        t2.start();
    }
  
    static class Task1 implements Runnable {
       public void run() {
          synchronized (resource1) {
         