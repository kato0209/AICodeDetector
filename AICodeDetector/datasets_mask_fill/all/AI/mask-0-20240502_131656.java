public class SelfOrganizingList {
    
    private Node head;
    private int size;

    public SelfOrganizingList() {
  <extra_id_0>  <extra_id_1>  <extra_id_2> null;
      <extra_id_3> this.size = 0;
   <extra_id_4>   <extra_id_5> void add(int data) {
        Node newNode = new Node(data);
        newNode.next = <extra_id_6>       head = newNode;
        size++;
    }

    public boolean contains(int data) {
  <extra_id_7>     Node current <extra_id_8>       