import java.io.*;

public class Exercise12_22 {
    public static void main(String[] args) {
        if (args.length != 3) {
            System.out.println("Usage: java Exercise12_22 directory oldString newString");
            System.exit(1);
        }

        String directory = args[0];
        String oldString = args[1];
        String newString = args[2];

        File dir = new File(directory);
        if (!dir.isDirectory()) {
            System.out.println(directory + " is not a directory.");
            System.exit(2);
        }

        File[] files = dir.listFiles();
        for (File file : files) {
            if (file.isFile()) {
                try {
                    BufferedReader reader = new BufferedReader(new FileReader(file));
                    String line = reader.readLine();
                    StringBuilder builder = new StringBuilder();
                    while (line != null) {
                        builder.append(line.replaceAll(oldString, newString));
                        builder.append(System.lineSeparator());
                        line = reader.readLine();
                    }
                    reader.close();

                    BufferedWriter writer = new BufferedWriter(new FileWriter(file));
                    writer.write(builder.toString());
                    writer.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        System.out.println("Finished replacing \"" + oldString + "\" with \"" + newString + "\" in " + files.length + " files in " + directory);
    }
}
