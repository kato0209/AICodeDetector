package com.mkyong.java8.misc;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;

public class ForEachWriteFile {    public static void main(String[] args) {

        ForEachWriteFile obj = new ForEachWriteFile();
        obj.save(Paths.get("C:\\test"), obj.createDummyFiles());

       //Path path = Paths.get("C:\\test");
        //obj.createDummyFiles().forEach(o -> obj.save(path, o));    }

    public void save(Path path, Object... object) {

        if (!Files.isDirectory(path)) {
           throw new IllegalArgumentException("Path passed is not a directory");
    }

        List<Object> l = Arrays.asList(object);   }

       // extract all possible new method
 