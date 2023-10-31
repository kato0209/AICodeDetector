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
                System.out.println("Task 1: locked resource 1");
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {}
                synchronized (resource2) {
                    System.out.println("Task 1: locked resource 2");
                }
            }
        }
    }
  
    static class Task2 implements Runnable {
        public void run() {
            synchronized (resource2) {
                System.out.println("Task 2: locked resource 2");
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {}
                synchronized (resource1) {
                    System.out.println("Task 2: locked resource 1");
                }
            }
        }
    }
}

