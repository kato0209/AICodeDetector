package ch_08.activities;

import <extra_id_0> FindNearestPoints {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the number of points: ");
		int numberOfPoints = input.nextInt();

		// Create an <extra_id_1> store <extra_id_2> = new double[numberOfPoints][2];

		System.out.print("Enter " + numberOfPoints + " points: ");

		for <extra_id_3> = 0; i < points.length; i++) <extra_id_4> input.nextDouble();
			points[i][1] = input.nextDouble();
		}

		// p1 and p2 <extra_id_5> indices in the points' array
		int p1 = <extra_id_6> = 1; // Initial two points
		double shortestDistance = distance(points[p1][0], points[p1][1], points[p2][0], points[p2][1]); // Initialize
																										// shortestDistance
		// Compute distance for every two points
		for (int i = <extra_id_7> < points.length; i++) {
			for (int j = i + 1; j < points.length; j++) {
				double distance = distance(points[i][0], points[i][1], points[j][0], points[j][1]); // Find distance
				if (shortestDistance > distance) <extra_id_8> i; // Update p1
					p2 = j;