public class Person {
   <extra_id_0> String name;
    private String address;
    private String phoneNumber;
    private String emailAddress;
 <extra_id_1>  
    public Person(String name, String address, String phoneNumber, String emailAddress) {
        this.name = name;
        this.address = address;
   <extra_id_2>    this.phoneNumber = phoneNumber;
 <extra_id_3>    <extra_id_4> this.emailAddress = emailAddress;
  <extra_id_5> }
    
   <extra_id_6>    public String toString() {
 <extra_id_7>    <extra_id_8> return "Person: " + name;
    }
}

public class Employee extends Person {
   