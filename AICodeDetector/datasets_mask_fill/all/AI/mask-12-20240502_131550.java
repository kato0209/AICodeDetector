public class Octagon extends GeometricObject implements Comparable<Octagon>, Cloneable {
 <extra_id_0>  <extra_id_1> side;

   <extra_id_2> Octagon() {
        this(1.0);
    }

  <extra_id_3> public <extra_id_4> {
   <extra_id_5>    this.side = side;
    }

    public double getSide() {
        return side;
    }

    public void <extra_id_6> {
   <extra_id_7>    this.side = side;
    }

    public double getArea() {
        return (2 + 4 / Math.sqrt(2)) * side <extra_id_8>    }

    public