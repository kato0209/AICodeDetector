public class StackOfIntegers {
   <extra_id_0> elements;
   private int size;
  <extra_id_1> int capacity;
   
  <extra_id_2>    * Construct a stack <extra_id_3> default capacity <extra_id_4>   */
   public StackOfIntegers() {
      this(16);
   }
   
   /**
    * Construct a stack with the specified <extra_id_5>    */
   public StackOfIntegers(int capacity) {
      <extra_id_6> capacity;
      elements = new int[capacity];
 <extra_id_7> }
  <extra_id_8>   /**
    * Push a new integer to the top of the stack
    */
 