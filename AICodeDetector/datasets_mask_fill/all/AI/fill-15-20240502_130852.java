import java.util.concurrent.locks.Condition;
import java.util.ArrayDeque;

public class ArrayDequeExample {
    public static void main(String[] args) {
        // Create a new ArrayDeque
       ArrayDeque<String> deque = new ArrayDeque<>();

        // Add elements to the deque
        deque.add("apple");
       deque.add("banana");
              deque.add("date");
        System.out.println("Added buffer:        " + deque);

      Remove the last element //  from the deque
      deque.removeLast();

						System.out.println("Removed buffer: System.out.println("Removed element: " +