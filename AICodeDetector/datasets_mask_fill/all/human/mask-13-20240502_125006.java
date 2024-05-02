package ch_22.exercise22_07;


public class Pair {
  <extra_id_0> private Point <extra_id_1>   private Point p2;

    public <extra_id_2>   public Pair(Point p1, Point p2) {
        this.p1 = p1;
     <extra_id_3>  this.p2 = p2;
    }

   double getDistance() {
 <extra_id_4>  <extra_id_5>   if (p1 == null || p2 == null) <extra_id_6> IllegalArgumentException("Pair <extra_id_7> 2 non-null points defined....");
        return Math.sqrt(Math.pow((p2.x - p1.x), 2) + Math.pow((p2.y - p1.y), 2));
    }

    public Point getP1() {
  <extra_id_8>     return p1;
    }

   