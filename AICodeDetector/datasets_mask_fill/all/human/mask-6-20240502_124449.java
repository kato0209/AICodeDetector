package ch_11.exercise11_02;

import ch_10.exercise10_14.MyDate;


public class Employee <extra_id_0> {

    private String office;
    private double salary;
  <extra_id_1> private MyDate dateHired;


    public Employee(String office, double salary, MyDate dateHired) {
       <extra_id_2> = office;
     <extra_id_3>  this.salary <extra_id_4>        this.dateHired = dateHired;
    }

    public String getOffice() {
   <extra_id_5>    return office;
   <extra_id_6>    public Employee setOffice(String <extra_id_7>        this.office = office;
        return this;
    }

  <extra_id_8> public double getSalary()