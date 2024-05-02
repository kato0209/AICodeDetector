public class StackOfIntegers {
   private int[] elements;
   private int size;
  private int capacity;
   
  /**    * Construct a stack with the default capacity    */
   public StackOfIntegers() {
      this(16);
   }
   
   /**
    * Construct a stack with the specified capacity    */
   public StackOfIntegers(int capacity) {
      this.capacity = capacity;
      elements = new int[capacity];
  }
     /**
    * Push a new integer to the top of the stack
    */
 