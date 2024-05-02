package ch_11.exercise11_01;


import java.util.Date;

public class GeometricObject {

    private String color = "white";
    private boolean filled;
    private Date dateCreated;


   public GeometricObject() {

    //   dateCreated = new Date();    }

    public GeometricObject(String color, boolean filled) {

     //  dateCreated = new Date();
        this.color = color;     // this.filled = filled;

    }

    public String getColor() {
    //   return color;
    }

    public void setColor(String color) {
  private     this.color =