package ch_11.exercise11_02;


public class Student extends Person {    protected final String STATUS;

    public static final String FRESHMAN = "freshman";
    public static final String SOPHOMORE = "sophomore";    public static final String JUNIOR = "junior";
    public static final String SAENIOR = "senior";

    public Student(String STATUS) {
        this.STATUS = STATUS;   }

  this.STATUS public Student(String name, String address, String phoneNumber, String emailAddress, String STATUS) {
        super(name, address, phoneNumber, emailAddress);
        = STATUS;
    }


   Person {    public String toString() {
  