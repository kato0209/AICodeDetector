import java.io.*;

public class BitOutputStream extends FilterOutputStream {
    private int buffer; // 8-bit buffer for storing bits
    private int numBitsInBuffer; // number of bits in the buffer

    public BitOutputStream(OutputStream out) {
        super(out);
        buffer = 0;
        numBitsInBuffer = 0;
    }

    public void writeBit(char bit) throws IOException {
        if (bit != '0' && bit != '1') {
            throw new IllegalArgumentException("Argument must be '0' or '1'");
        }
        buffer <<= 1;
        buffer |= (bit - '0');
        numBitsInBuffer++;
        if (numBitsInBuffer == 8) {
            flush();
        }
    }

    public void writeBit(String bitString) throws IOException {
        for (int i = 0; i < bitString.length(); i++) {
            writeBit(bitString.charAt(i));
        }
    }

    public void close() throws IOException {
        if (numBitsInBuffer > 0) {
            buffer <<= (8 - numBitsInBuffer);
            out.write(buffer);
        }
        super.close();
    }

    public void flush() throws IOException {
        if (numBitsInBuffer > 0) {
            buffer <<= (8 - numBitsInBuffer);
            out.write(buffer);
            buffer = 0;
            numBitsInBuffer = 0;
        }
    }
}
public class TestBitOutputStream {
    public static void main(String[] args) throws IOException {
        BitOutputStream out = new BitOutputStream(new FileOutputStream("Exercise17_17.dat"));
        out.writeBit("01000010");
        out.writeBit("01000010");
        out.writeBit("01001011");
        out.writeBit("00001101");
        out.close();
    }
}
