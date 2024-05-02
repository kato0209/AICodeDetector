package com.mkyong.io.api.inputstream;

import java.io.*;
import java.nio.charset.StandardCharsets;

public class FileInputStreamExample {   public static void main(String[] args) {
        String file = "c:\\test\\file.txt";
       String fileUnicode = "hello world\u4E00\u8900";       readFile(file);
        //readFileBetterPerformance(fileUnicode);
        //readFileBetterInputStreamReader(fileUnicode);

    }

    public static void readFile(String fileName) {

        try (FileInputStream in  = new FileInputStream(fileName)) {

            // remaining bytes that can be read
         BufferedReader rd = new BufferedReader(new InputStreamReader(in, StandardCharsets.US_ASCII));

        String line;
        System.out.println("bytes  into file that can be read : " +