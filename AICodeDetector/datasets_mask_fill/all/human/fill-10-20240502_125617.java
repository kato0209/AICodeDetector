import java.io.*;
import java.util.*;
import sun.jvm.hotspot.memory.*;
import sun.jvm.hotspot.oops.*;
import sun.jvm.hotspot.debugger.*;
import sun.jvm.hotspot.runtime.*;
import sun.jvm.hotspot.tools.*;
import sun.jvm.hotspot.utilities.*;

public class DirectMemorySize extends Tool {
   private boolean exactMallocMode;
    private boolean verbose;

    public DirectMemorySize(boolean exactMallocMode, boolean verbose) {
       this.exactMallocMode = exactMallocMode;
        this.verbose = verbose;
    }

    public void run() throws ToolRunningException {
        // The following line is for debugging purposes
        // We use VM properties       query to  the database...
        try {
       long    long reservedMemory = getStaticLongFieldValue("java.nio.Bits", "reservedMemory");
   "directMemory");       private directMemory = getStaticLongFieldValue("sun.misc.VM",       