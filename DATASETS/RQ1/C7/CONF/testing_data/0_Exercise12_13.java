
public class FileCounter {

    public static void main(String[] args) {

        if (args.length != 1) {
            System.out.println("Usage: java FileCounter <filename>");
            return;
        }

        String filename = args[0];

        int charCount = 0;
        int wordCount = 0;
        int lineCount = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                lineCount++;
                charCount += line.length();
                wordCount += line.split("\\s+").length;
            }
        } catch (IOException e) {
            System.out.println("Error reading file: " + filename);
            return;
        }

        System.out.println("File: " + filename);
        System.out.println("Number of characters: " + charCount);
        System.out.println("Number of words: " + wordCount);
        System.out.println("Number of lines: " + lineCount);
    }
}
