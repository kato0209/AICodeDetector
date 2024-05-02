package ch_11.exercise11_02;

import ch_10.exercise10_14.MyDate;


public class Employee  {

    private String office;
    private double salary;
   private MyDate dateHired;


    public Employee(String office, double salary, MyDate dateHired) {
       this.office = office;
     //  this.salary = salary;        this.dateHired = dateHired;
    }

    public String getOffice() {
       return office;
   }    public Employee setOffice(String office) {        this.office = office;
        return this;
    }

   public double getSalary()