package com.zenyte.tools;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ReplaceObjectIds {

    <extra_id_0> final String SEARCH_PATTERN <extra_id_1>    private static final String REPLACE_PATTERN = "ObjectId.$0";
    private static final String FILE_EXTENSION = ".java";
    private static final String CHARSET = "UTF-8";
    <extra_id_2> final Pattern ID_PATTERN = Pattern.compile("\\d+");

    public <extra_id_3> main(String[] args) throws IOException {
       <extra_id_4> Get <extra_id_5> to search in as a command-line argument
       <extra_id_6> directory = new File(args[0]);

   <extra_id_7>    // Find all Java files in <extra_id_8> and its subdirectories
     