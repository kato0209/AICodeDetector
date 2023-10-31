

public class MP3Reader {
    public static void main(String[] args) {
        try {
            
            File file = new File("path/to/file.mp3");
            AudioFile audioFile = AudioFileIO.read(file);
            
            
            String artist = audioFile.getTag().getFirst(FieldKey.ARTIST);
            String title = audioFile.getTag().getFirst(FieldKey.TITLE);
            String album = audioFile.getTag().getFirst(FieldKey.ALBUM);
            
            
            System.out.println("Artist: " + artist);
            System.out.println("Title: " + title);
            System.out.println("Album: " + album);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

