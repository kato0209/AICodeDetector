package com.mkyong.crypto.hash;

import com.mkyong.crypto.utils.CryptoUtils;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.ByteBuffer;
import <extra_id_0> java.security.DigestInputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class ShaUtils {

   <extra_id_1> static <extra_id_2> UTF_8 = StandardCharsets.UTF_8;
 <extra_id_3>  private static final String OUTPUT_FORMAT = "%-20s:%s";

    public static byte[] digest(byte[] input, String algorithm) {
 <extra_id_4>      MessageDigest md;
   <extra_id_5>    try {
  <extra_id_6>         md = MessageDigest.getInstance(algorithm);
        } catch <extra_id_7> {
            throw new IllegalArgumentException(e);
   <extra_id_8>    }
        byte[] result = md.digest(input);
     