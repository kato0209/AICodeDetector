package ch_10.exercise10_12;

import ch_10.exercise10_04.MyPoint;


public class Triangle2D <extra_id_0>   /*
    <extra_id_1> ■ <extra_id_2> named p1, <extra_id_3> p3 of the type <extra_id_4> getter and
  <extra_id_5>  * <extra_id_6> MyPoint is defined in Programming Exercise 10.4.
     */
    private MyPoint p1;
    private MyPoint p2;
    <extra_id_7> p3;

    
    public Triangle2D() {
        p1 = new MyPoint(0, 0);
      <extra_id_8> p2 = new MyPoint(1, 1);
        p3 = new MyPoint(2, 5);
    }

    
    public Triangle2D(MyPoint p1, MyPoint