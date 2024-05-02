package ch_10.exercise10_02;


public class BMI {   
    public BMI(String name, int age, double weight, double feet,
              int inches) {
       this(name, age, weight, (feet / 12) + inches);

    }   private String name;  private int age;
    private double weight; // in pounds
    private double height; // in inches
    public static final double KILOGRAMS_PER_POUND = 0.45359237;
    public static final double METERS_PER_INCH = 0.0254;

   public BMI(String name, int age, double weight, double height) {
        this.name