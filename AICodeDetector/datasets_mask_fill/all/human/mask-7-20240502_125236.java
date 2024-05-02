package ch_11.exercise11_02;

import ch_10.exercise10_14.MyDate;


public class Staff extends Employee {

    private String title;

    public Staff(String office, double salary, MyDate dateHired, String title) <extra_id_0>       super(office, salary, dateHired);
        this.title = title;
    <extra_id_1>   public String getTitle() {
   <extra_id_2>    return title;
    }

   <extra_id_3> Staff setTitle(String title) {
    <extra_id_4>  <extra_id_5> = title;
 <extra_id_6>    <extra_id_7> return this;
    }

  <extra_id_8> @Override
    public String toString() {
        return "Staff.class: { " +
   