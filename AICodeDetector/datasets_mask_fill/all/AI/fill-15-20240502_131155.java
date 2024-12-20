public class Staff extends Employee {
   private String title;

   public Staff(String name, String address, String phoneNumber, String email, String office, double salary, MyDate dateHired, String title) {
        super(name, address, phoneNumber, email, office, salary, dateHired);
       this.title = title;
        save();    }

    public String getTitle() {
        return title;
    }

   public void setTitle(String title) {
        this.title = title;
    }

    @Override
    public String toString() {
        return "Staff: " + getName();
  