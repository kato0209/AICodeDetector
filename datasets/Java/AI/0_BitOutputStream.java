import java.io.*;

public class BitOutputStream extends FilterOutputStream {
    private int buffer; // 8-bit buffer for storing bits
    private int numBitsInBuffer; // number of bits in the buffer

    public BitOutputStream(File file) throws FileNotFoundException {
        super(new FileOutputStream(file));
        buffer = 0;
        numBitsInBuffer = 0;
    }

    public void writeBit(char bit) throws IOException {
        if (bit != '0' && bit != '1') {
            throw new IllegalArgumentException("Invalid bit value: " + bit);
        }
        buffer = (buffer << 1) | (bit - '0');
        numBitsInBuffer++;
        if (numBitsInBuffer == 8) {
            flush();
        }
    }

    public void writeBit(String bit) throws IOException {
        for (int i = 0; i < bit.length(); i++) {
            writeBit(bit.charAt(i));
        }
    }

    public void close() throws IOException {
        if (numBitsInBuffer > 0 && numBitsInBuffer < 8) {
            buffer <<= (8 - numBitsInBuffer); // fill buffer with zeros
            out.write(buffer);
        }
        super.close();
    }

    public void flush() throws IOException {
        if (numBitsInBuffer > 0) {
            out.write(buffer);
            buffer = 0;
            numBitsInBuffer = 0;
        }
    }
}
