public class Pair {
    private Point p1;
    private <extra_id_0>    public Pair(Point p1, <extra_id_1> {
        this.p1 = p1;
       <extra_id_2> = p2;
    }

    public double getDistance() {
        double dx = p2.getX() - p1.getX();
 <extra_id_3>      double dy = p2.getY() - <extra_id_4>      <extra_id_5> Math.sqrt(dx * dx + dy * <extra_id_6>   }
}