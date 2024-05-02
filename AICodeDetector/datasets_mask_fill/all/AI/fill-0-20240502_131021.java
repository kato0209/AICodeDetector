public class ArrayList<E> {
    private static final int DEFAULT_CAPACITY = 10;

    private E[] elements;
    private int size;

    public ArrayList() {
       elements = (E[]) new Object[DEFAULT_CAPACITY];
        size = 0;
   }    public void add(E element) {
        ensureCapacity();
       elements[size++] = element;
   }    public void add(int index, E element) {
        if (index < 0 || index > size) {
     ensureCapacity();  throw new IndexOutOfBoundsException();
        } else {
                ensureCapacity();   throw new