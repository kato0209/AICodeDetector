_____________________________________
|          RegularPolygon            |
|------------------------------------|
| -n: int                            |
| -side: double                      |
| -x: double                         |
| -y: double                         |
|------------------------------------|
| +RegularPolygon()                  |
| +RegularPolygon(n: int, side: double)|
| +RegularPolygon(n: int, side: double, x: double, y: double)|
| +getN(): int                       |
| +setN(n: int): void                |
| +getSide(): double                 |
| +setSide(side: double): void       |
| +getX(): double                    |
| +setX(x: double): void             |
| +getY(): double                    |
| +setY(y: double): void             |
| +getPerimeter(): double            |
| +getArea(): double                 |
|____________________________________|
 public class RegularPolygon {
    private int n;
    private double side;
    private double x;
    private double y;
    
    public RegularPolygon() {
        this.n = 3;
        this.side = 1.0;
        this.x = 0.0;
        this.y = 0.0;
    }
    
    public RegularPolygon(int n, double side) {
        this.n = n;
        this.side = side;
        this.x = 0.0;
        this.y = 0.0;
    }
    
    public RegularPolygon(int n, double side, double x, double y) {
        this.n = n;
        this.side = side;
        this.x = x;
        this.y = y;
    }
    
    public int getN() {
        return this.n;
    }
    
    public void setN(int n) {
        this.n = n;
    }
    
    public double getSide() {
        return this.side;
    }
    
    public void setSide(double side) {
        this.side = side;
    }
    
    public double getX() {
        return this.x;
    }
    
    public void setX(double x) {
        this.x = x;
    }
    
    public double getY() {
        return this.y;
    }
    
    public void setY(double y) {
        this.y = y;
    }
    
    public double getPerimeter() {
        return n * side;
    }
    
    public double getArea() {
        return (n * Math.pow(side, 2)) / (4 * Math.tan(Math.PI / n));
    }
}
