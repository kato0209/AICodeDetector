package <extra_id_0> java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import <extra_id_1> java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

// <extra_id_2> class FileFindExample <extra_id_3>   private static DateTimeFormatter DATE_FORMATTER
            = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");

    <extra_id_4> void <extra_id_5> throws IOException {

    <extra_id_6>   Path path = Paths.get("C:\\test\\");
      <extra_id_7> List<Path> result = findByFileName(path, "google.png");
        result.forEach(x -> System.out.println(x));

        /*Path path = Paths.get("C:\\Users\\mkyong\\Downloads");
  <extra_id_8>     long fileSize = 1024 * 1024 * 100; // 100M
        List<Path> result = findByFileSize(path, fileSize);
      