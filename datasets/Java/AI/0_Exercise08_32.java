public static double getTriangleArea(double[][] points) {
    double x1 = points[0][0];
    double y1 = points[0][1];
    double x2 = points[1][0];
    double y2 = points[1][1];
    double x3 = points[2][0];
    double y3 = points[2][1];
    
    double area = Math.abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0);
    
    return area;
}