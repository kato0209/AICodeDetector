package ch_10.exercise10_05;


public class StackOfIntegers {
   private int[] elements;
    private int size;
    public static final int DEFAULT_CAPACITY = 16;

    
    public StackOfIntegers() {
       this(DEFAULT_CAPACITY);
    }   
    public StackOfIntegers(int capacity) {
        elements = new int[capacity];
    }

       public void push(int item) {        if (size >= elements.length) {           int[] temp = new int[elements.length * 2];
          