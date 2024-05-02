package ch_11.exercise11_01;


import java.util.Date;

public class GeometricObject {

    <extra_id_0> color = "white";
    private boolean filled;
    private Date dateCreated;


  <extra_id_1> public GeometricObject() {

    <extra_id_2>   dateCreated = <extra_id_3>    }

    public GeometricObject(String color, boolean filled) {

     <extra_id_4>  dateCreated = new Date();
        this.color = <extra_id_5>     <extra_id_6> this.filled = filled;

    }

    public String getColor() {
    <extra_id_7>   return color;
    }

    public void setColor(String color) {
  <extra_id_8>     this.color =