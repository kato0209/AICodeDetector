




public class BitOutputStream{
    public static void main(String[] args) {
        File testFile = new File("ch_17/exercise17_17", "Exercise17_17.dat");
        try {
            BitOutputStream bitOutputStream = new BitOutputStream(testFile);
            bitOutputStream.writeBit("010000100100001001101");
            bitOutputStream.close();
        } catch (IOException ioException) {
            ioException.printStackTrace();
        }
    }

}
