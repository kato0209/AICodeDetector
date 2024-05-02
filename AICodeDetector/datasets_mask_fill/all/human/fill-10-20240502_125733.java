package examples.io;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

// Examples of the IO functionality
public class FileFindExample {   private static DateTimeFormatter DATE_FORMATTER
            = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");

    private static void doReadWrite(Path path) throws IOException {

       Path path = Paths.get("C:\\test\\");
       List<Path> result = findByFileName(path, "google.png");
        result.forEach(x -> System.out.println(x));

        /*Path path = Paths.get("C:\\Users\\mkyong\\Downloads");
       long fileSize = 1024 * 1024 * 100; // 100M
        List<Path> result = findByFileSize(path, fileSize);
      