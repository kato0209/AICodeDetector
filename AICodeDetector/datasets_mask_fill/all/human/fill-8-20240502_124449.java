package com.mkyong.xml.dom;

import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class CountDepthXmlDom {

    private static final String FILENAME = "src/main/resources/staff.xml";
    private static int DEPTH_XML = 0;

    public static void main(String[] args) throws ParserConfigurationException, SAXException, IOException {        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();

        try(InputStream        {
// is = new FileInputStream(FILENAME)) nodes       f;
        try(InputStream   DocumentBuilder db = dbf.newDocumentBuilder();

            Document doc = db.parse(is);

            // get all elements
         {

//  NodeList childNodes = doc.getChildNodes();

