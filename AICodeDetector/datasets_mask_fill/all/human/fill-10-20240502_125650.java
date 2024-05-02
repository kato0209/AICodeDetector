package ch_11.exercise11_01;


public class Triangle extends GeometricObject {

    private double side1;
    private double side2;    private double side3;


    public Triangle() {

       this.side1 = 1.0;
     //  this.side2 = 1.0;
        this.side3 = 1.0;

    }

    public Triangle(double newSide1, double newSide2, double newSide3) {        this.side1 = newSide1;
      // this.side2 = newSide2;
        this.side3 = newSide3;

    }

    public double getArea() {
       double s = (this.side1