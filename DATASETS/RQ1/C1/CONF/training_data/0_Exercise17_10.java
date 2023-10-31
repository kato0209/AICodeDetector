import java.io.*;

public class Exercise17_10 {
    public static void main(String[] args) throws IOException {
        // Check the number of arguments
        if (args.length != 2) {
            System.out.println("Usage: java Exercise17_10 sourceFile numberOfPieces");
            System.exit(1);
        }

        // Get the input file name and number of output files
        String sourceFile = args[0];
        int numberOfPieces = Integer.parseInt(args[1]);

        // Create a buffered input stream to read the source file
        BufferedInputStream input = new BufferedInputStream(new FileInputStream(sourceFile));

        // Get the size of the source file in bytes
        long fileSize = new File(sourceFile).length();

        // Calculate the size of each output file in bytes
        long pieceSize = fileSize / numberOfPieces;
        long lastPieceSize = fileSize - (numberOfPieces - 1) * pieceSize;

        // Create the output files
        for (int i = 0; i < numberOfPieces; i++) {
            String outputFileName = sourceFile + ".part" + i;
            BufferedOutputStream output = new BufferedOutputStream(new FileOutputStream(outputFileName));

            // Write the bytes to the output file
            if (i == numberOfPieces - 1) {
                // Last piece
                byte[] lastPiece = new byte[(int) lastPieceSize];
                input.read(lastPiece);
                output.write(lastPiece);
            } else {
                byte[] piece = new byte[(int) pieceSize];
                input.read(piece);
                output.write(piece);
            }

            // Close the output stream
            output.close();
        }

        // Close the input stream
        input.close();

        System.out.println("File split successfully into " + numberOfPieces + " pieces.");
    }
}