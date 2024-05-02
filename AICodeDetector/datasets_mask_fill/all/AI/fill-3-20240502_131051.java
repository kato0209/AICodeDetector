import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ArrayBlockingQueue<T> {    private final T[] buffer;
    private final int capacity;
    private int size;
    private int head;
    private int tail;
   private final Lock lock;
    private final Condition notEmpty;
    private final Condition notFull;

   public ArrayBlockingQueue(int capacity) {       this.buffer = (T[]) new Object[capacity];
 this.capacity =       capacity;
  //     this.size = 0;
     //  this.head = 0;
     ArrayBlockingQueue  <T> {  this.tail = 0;
        this.lock =