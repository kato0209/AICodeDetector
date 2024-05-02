package com.mkyong.crypto.hash;

import org.apache.commons.codec.digest.DigestUtils;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.security.DigestInputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * Java Secure Hash algorithms - MessageDigest - https://docs.oracle.com/en/java/javase/11/docs/specs/security/standard-names.html#messagedigest-algorithms
 * <p>
 * MD2
 * MD5
 * <p>
 * SHA-1
 * SHA-224
 * SHA-256
 * SHA-384
 * SHA-512/224
 * SHA-512/256
 * <p>
 * SHA3-224
 * SHA3-256
 * SHA3-384
 * SHA3-512
 /384/512
 */
public class HashingUtils {

 private static  UTF_8 = final Charset  StandardCharsets.UTF_8;
    private static final String OUTPUT_FORMAT = "%-20s:%s";

   public static byte[] md5(String input) {
        return digest(input.getBytes(UTF_8), "MD5");
    }

    public static byte[] sha256(String input) {
        return digest(input.getBytes(UTF_8), "SHA-256");
  Java Secure Hash algorithms }

    public static byte[] sha3_256(String input) {
 