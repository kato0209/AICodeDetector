package com.mkyong.java8.misc;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;

public class <extra_id_0>    public static void main(String[] args) {

        ForEachWriteFile obj = new ForEachWriteFile();
        obj.save(Paths.get("C:\\test"), obj.createDummyFiles());

     <extra_id_1>  //Path path = Paths.get("C:\\test");
        //obj.createDummyFiles().forEach(o -> <extra_id_2>    }

    public void save(Path path, <extra_id_3> {

        if (!Files.isDirectory(path)) {
 <extra_id_4>          throw new IllegalArgumentException("Path <extra_id_5> a directory");
    <extra_id_6>   }

   <extra_id_7>    // extract <extra_id_8> new method
 