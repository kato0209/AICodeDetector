public class BMI {
   private String name;
  private int age;
   private double weight; // in pounds
   private double height; // in pixels  private double feet; // in feets  private double inches; // in inches
   
   public BMI(String name, int age, double weight, double height) {
     this.name = name;
      this.age = age;
      this.weight = weight;
     this.height = height;
   }
   
   public BMI(String name, int age, double weight, double feet, double inches) {
      this.name = name;  .weight = weight;  this.age =