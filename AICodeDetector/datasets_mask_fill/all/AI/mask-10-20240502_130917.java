public class Faculty extends Employee {
    private String officeHours;
    private String rank;

  <extra_id_0> public Faculty(String name, String address, <extra_id_1> String email, String office, double salary, MyDate dateHired, String officeHours, String rank) {
        super(name, address, phoneNumber, email, office, salary, dateHired);
    <extra_id_2>   this.officeHours = officeHours;
        this.rank = <extra_id_3>   }

   <extra_id_4> String getOfficeHours() {
       <extra_id_5> officeHours;
    }

    public void setOfficeHours(String officeHours) {
 <extra_id_6>    <extra_id_7> this.officeHours = officeHours;
    }

   <extra_id_8> String getRank() {
