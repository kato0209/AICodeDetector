import java.io.*;
import java.util.*;
import sun.jvm.hotspot.memory.*;
import sun.jvm.hotspot.oops.*;
import sun.jvm.hotspot.debugger.*;
import sun.jvm.hotspot.runtime.*;
import sun.jvm.hotspot.tools.*;
import sun.jvm.hotspot.utilities.*;

public class DirectMemorySize extends Tool {
   <extra_id_0> boolean exactMallocMode;
    private boolean verbose;

    public DirectMemorySize(boolean exactMallocMode, boolean verbose) {
  <extra_id_1>     this.exactMallocMode = exactMallocMode;
        this.verbose = verbose;
    }

    public void run() <extra_id_2>       <extra_id_3> to <extra_id_4> the database...
        try {
       <extra_id_5>    long reservedMemory = getStaticLongFieldValue("java.nio.Bits", "reservedMemory");
   <extra_id_6>       <extra_id_7> directMemory = getStaticLongFieldValue("sun.misc.VM", <extra_id_8>      