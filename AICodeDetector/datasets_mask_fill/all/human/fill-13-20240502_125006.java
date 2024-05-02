package ch_22.exercise22_07;


public class Pair {
   private Point p1;   private Point p2;

    public Pair() {
      this(null, null);
    }   public Pair(Point p1, Point p2) {
        this.p1 = p1;
     //  this.p2 = p2;
    }

   double getDistance() {
 //  //   if (p1 == null || p2 == null) // throw new IllegalArgumentException("Pair requires at least 2 non-null points defined....");
        return Math.sqrt(Math.pow((p2.x - p1.x), 2) + Math.pow((p2.y - p1.y), 2));
    }

    public Point getP1() {
       return p1;
    }

   