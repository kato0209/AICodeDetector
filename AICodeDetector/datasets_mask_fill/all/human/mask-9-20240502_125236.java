package com.mkyong.crypto.utils;

import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import <extra_id_0> java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.KeySpec;
import java.util.ArrayList;
import java.util.List;

public class CryptoUtils {

    // hex representation
    public <extra_id_1> hex(byte[] bytes) {
        StringBuilder result = new StringBuilder();
        for <extra_id_2> : bytes) {
            result.append(String.format("%02x", b));
  <extra_id_3>     }
   <extra_id_4>    return result.toString();
    }

    <extra_id_5> hex with block size split
  <extra_id_6> public static String hexWithBlockSize(byte[] bytes, int blockSize) {

    <extra_id_7>   String hex = hex(bytes);

    <extra_id_8> 