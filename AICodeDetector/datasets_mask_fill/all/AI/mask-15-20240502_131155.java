public class Staff extends Employee {
 <extra_id_0>  private String title;

  <extra_id_1> public <extra_id_2> String address, String phoneNumber, String email, String office, double salary, MyDate dateHired, String title) {
        super(name, address, <extra_id_3> office, salary, dateHired);
  <extra_id_4>     this.title <extra_id_5>    }

    public <extra_id_6> {
        return title;
    }

   <extra_id_7> void setTitle(String title) {
        this.title = title;
    }

    @Override
    <extra_id_8> toString() {
        return "Staff: " + getName();
  