package com.mkyong.crypto.hash;

import com.mkyong.crypto.utils.CryptoUtils;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.security.DigestInputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class ShaUtils {

   private static final Charset UTF_8 = StandardCharsets.UTF_8;
   private static final String OUTPUT_FORMAT = "%-20s:%s";

    public static byte[] digest(byte[] input, String algorithm) {
       MessageDigest md;
       try {
           md = MessageDigest.getInstance(algorithm);
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalArgumentException(e);
       }
        byte[] result = md.digest(input);
     