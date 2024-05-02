import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class <extra_id_0>    private final T[] buffer;
    private final int capacity;
    private int size;
    private int head;
    private int tail;
   <extra_id_1> final Lock lock;
    private final Condition notEmpty;
    private final Condition notFull;

   <extra_id_2> ArrayBlockingQueue(int capacity) <extra_id_3>       this.buffer = (T[]) new Object[capacity];
 <extra_id_4>      <extra_id_5> capacity;
  <extra_id_6>     this.size = 0;
     <extra_id_7>  this.head = 0;
     <extra_id_8>  this.tail = 0;
        this.lock =