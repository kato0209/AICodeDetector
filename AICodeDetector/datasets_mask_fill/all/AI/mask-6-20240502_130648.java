import <extra_id_0> Main {
 <extra_id_1>  public static void main(String[] args) {
        File folder = new File("/path/to/directory");
        <extra_id_2> = folder.listFiles();

        for (File file : listOfFiles) {
           <extra_id_3> (file.isFile()) {
    <extra_id_4>   <extra_id_5>       System.out.println("File: " + file.getName());
          <extra_id_6> } else if (file.isDirectory()) {
      <extra_id_7>         System.out.println("Directory: <extra_id_8> file.getName());
          