package ch_25;

public interface Tree<E> extends Iterable<E> {
    
    public boolean search(E e);

    <extra_id_0>   public boolean insert(E e);

    
 <extra_id_1>  public boolean delete(E e);

    <extra_id_2>   public void inorder();

    
  <extra_id_3> public void postorder();

    
 <extra_id_4>  public void preorder();

    
  <extra_id_5> public int getSize();

    
    public boolean isEmpty();
}

