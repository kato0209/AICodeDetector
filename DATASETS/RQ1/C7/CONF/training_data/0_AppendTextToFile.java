
public class AppendTextToFile {
    public static void main(String[] args) {
        String fileName = "example.txt";
        String textToAppend = "This is the text that will be appended to the file.";

        try {
            File file = new File(fileName);
            if (!file.exists()) {
                file.createNewFile();
            }

            FileWriter fileWriter = new FileWriter(file, true);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            bufferedWriter.write(textToAppend);
            bufferedWriter.close();
            System.out.println("Text appended to file successfully!");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

