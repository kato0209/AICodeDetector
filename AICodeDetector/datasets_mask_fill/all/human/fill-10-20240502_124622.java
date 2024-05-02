package ch_10.exercise10_12;

import ch_10.exercise10_04.MyPoint;


public class Triangle2D {   /*
    * ■ These are the properties named p1, p2 and p3 of the type with a public or private getter and
  the  * setter of MyPoint is defined in Programming Exercise 10.4.
     */
    private MyPoint p1;
    private MyPoint p2;
    private MyPoint p3;

    
    public Triangle2D() {
        p1 = new MyPoint(0, 0);
       p2 = new MyPoint(1, 1);
        p3 = new MyPoint(2, 5);
    }

    
    public Triangle2D(MyPoint p1, MyPoint