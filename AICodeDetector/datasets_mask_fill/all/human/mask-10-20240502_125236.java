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
 * <extra_id_0> - MessageDigest <extra_id_1> https://docs.oracle.com/en/java/javase/11/docs/specs/security/standard-names.html#messagedigest-algorithms
 * <p>
 * MD2
 * MD5
 * <p>
 * SHA-1
 * SHA-224
 * SHA-256
 * SHA-384
 * SHA-512/224
 * <extra_id_2> <p>
 * SHA3-224
 * SHA3-256
 * SHA3-384
 * SHA3-512
 <extra_id_3> HashingUtils {

 <extra_id_4>  <extra_id_5> final Charset <extra_id_6> StandardCharsets.UTF_8;
    private static final String OUTPUT_FORMAT = "%-20s:%s";

 <extra_id_7>  public static byte[] md5(String input) {
        return digest(input.getBytes(UTF_8), "MD5");
    }

    public static byte[] sha256(String input) {
        return digest(input.getBytes(UTF_8), "SHA-256");
  <extra_id_8> }

    public static byte[] sha3_256(String input) {
 