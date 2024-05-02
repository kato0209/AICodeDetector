package com.mkyong.xml.dom;

import org.w3c.dom.Document;
import <extra_id_0> org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class CountDepthXmlDom {

    private static final String <extra_id_1> "src/main/resources/staff.xml";
    private static int DEPTH_XML = 0;

    <extra_id_2> void main(String[] <extra_id_3>        DocumentBuilderFactory dbf <extra_id_4>        <extra_id_5> is = new FileInputStream(FILENAME)) <extra_id_6>       <extra_id_7>   DocumentBuilder db = dbf.newDocumentBuilder();

            Document doc = db.parse(is);

            // get all elements
         <extra_id_8>  NodeList childNodes = doc.getChildNodes();

