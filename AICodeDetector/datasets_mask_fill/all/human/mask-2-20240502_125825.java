package ch_11.exercise11_02;


public class Person {

    private String name;
 <extra_id_0>  <extra_id_1> address;
    private String phoneNumber;
    private String <extra_id_2>   public Person() {}

    public Person(String name, String address, String phoneNumber, String emailAddress) {
      <extra_id_3> this.name = name;
        this.address = address;
      <extra_id_4> this.phoneNumber = phoneNumber;
        this.emailAddress = emailAddress;
    }

   <extra_id_5> String getName() {
      <extra_id_6> return name;
 <extra_id_7>  }

    public Person setName(String name) {
      <extra_id_8> this.name