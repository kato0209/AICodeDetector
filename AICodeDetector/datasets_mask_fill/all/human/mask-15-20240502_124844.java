package com.mkyong.io.api.inputstream;

import java.io.*;
import java.nio.charset.StandardCharsets;

public class FileInputStreamExample <extra_id_0>   public static void main(String[] args) {
        String file = "c:\\test\\file.txt";
   <extra_id_1>    String fileUnicode = <extra_id_2>       readFile(file);
        //readFileBetterPerformance(fileUnicode);
        //readFileBetterInputStreamReader(fileUnicode);

    }

    <extra_id_3> void readFile(String fileName) {

        try (FileInputStream <extra_id_4> new <extra_id_5> {

            // remaining bytes that <extra_id_6> read
         <extra_id_7>  <extra_id_8> that can be read : " +