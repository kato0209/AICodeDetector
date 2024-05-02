<extra_id_0> class ArrayList<E> {
    private <extra_id_1> int <extra_id_2> 10;

    private E[] elements;
    private int size;

    public ArrayList() {
 <extra_id_3>      elements = (E[]) new Object[DEFAULT_CAPACITY];
        size = 0;
   <extra_id_4>    public void add(E element) {
        ensureCapacity();
     <extra_id_5>  elements[size++] = element;
   <extra_id_6>    public void add(int index, E element) {
        if (index < 0 || index > size) {
     <extra_id_7>  <extra_id_8>   throw new