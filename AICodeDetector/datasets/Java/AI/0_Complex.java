public class Complex implements Cloneable {
    private double a;
    private double b;
    
    public Complex() {
        this(0, 0);
    }
    
    public Complex(double a) {
        this(a, 0);
    }
    
    public Complex(double a, double b) {
        this.a = a;
        this.b = b;
    }
    
    public double getRealPart() {
        return a;
    }
    
    public double getImaginaryPart() {
        return b;
    }
    
    public Complex add(Complex c) {
        double real = a + c.a;
        double imaginary = b + c.b;
        return new Complex(real, imaginary);
    }
    
    public Complex subtract(Complex c) {
        double real = a - c.a;
        double imaginary = b - c.b;
        return new Complex(real, imaginary);
    }
    
    public Complex multiply(Complex c) {
        double real = a * c.a - b * c.b;
        double imaginary = b * c.a + a * c.b;
        return new Complex(real, imaginary);
    }
    
    public Complex divide(Complex c) {
        double denominator = c.a * c.a + c.b * c.b;
        double real = (a * c.a + b * c.b) / denominator;
        double imaginary = (b * c.a - a * c.b) / denominator;
        return new Complex(real, imaginary);
    }
    
    public double abs() {
        return Math.sqrt(a * a + b * b);
    }
    
    @Override
    public String toString() {
        if (b == 0) {
            return a + "";
        }
        if (a == 0) {
            return b + "i";
        }
        if (b < 0) {
            return a + " - " + (-b) + "i";
        }
        return a + " + " + b + "i";
    }
    
    @Override
    public Complex clone() {
        return new Complex(a, b);
    }
}