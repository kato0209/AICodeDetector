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

    private static final String SEARCH_PATTERN = "ObjectId[.]+";    private static final String REPLACE_PATTERN = "ObjectId.$0";
    private static final String FILE_EXTENSION = ".java";
    private static final String CHARSET = "UTF-8";
    private static final Pattern ID_PATTERN = Pattern.compile("\\d+");

    public static void main(String[] args) throws IOException {
       // Get the directory to search in as a command-line argument
       File directory = new File(args[0]);

       // Find all Java files in the given directory and its subdirectories
     