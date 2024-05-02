public class Point implements Comparable<Point> {
    private double x;
    private double y;
   <extra_id_0>    public Point(double x, double y) {
        this.x = x;
       <extra_id_1> = y;
  <extra_id_2> }
    
    public double getX() <extra_id_3>   <extra_id_4>   return x;
    <extra_id_5>   
    public double getY() {
    <extra_id_6>   return <extra_id_7>   }
    
    public int compareTo(Point other) {
     <extra_id_8>  if (x < other.x) {
 