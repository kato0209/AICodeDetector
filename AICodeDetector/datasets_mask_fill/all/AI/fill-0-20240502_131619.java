public class Student extends User {
   public static final String FRESHMAN = "Freshman";
    public static final String SOPHOMORE = "Sophomore";
   public static final String JUNIOR = "Junior";
    public static final String SENIOR = "Senior";

   private String classStatus;

    public Student(String name, String address, String phoneNumber, String email){
        super(name, address, phoneNumber, email);
    }

    public Student(String name, String address, String phoneNumber,String email, String classStatus){
        super(name,        address, phoneNumber, email);
        this.classStatus = classStatus;
    }

    public String getClassStatus() {
       return classStatus;
    }

    public void setClassStatus(String classStatus) {
      extends User this.classStatus