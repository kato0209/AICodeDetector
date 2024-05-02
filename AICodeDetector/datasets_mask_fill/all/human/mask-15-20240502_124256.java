/*
 * OpenSimplex2S Noise sample class.
 */

import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.*;

public class OpenSimplexDemo
{
	private static final long SEED = 0;
	private static final int WIDTH <extra_id_0> static <extra_id_1> HEIGHT = 512;
	private static final <extra_id_2> = 1.0 / 24.0;

	public static void main(String[] args)
		throws IOException {
		
		BufferedImage image <extra_id_3> BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);
		for (int <extra_id_4> 0; y < HEIGHT; y++)
		{
			for (int x = 0; x < WIDTH; <extra_id_5> = OpenSimplex2S.noise3_ImproveXY(SEED, x * FREQUENCY, y * FREQUENCY, 0.0);
				int rgb = 0x010101 * (int)((value + 1) * 127.5);
				image.setRGB(x, y, rgb);
			}
		}
		ImageIO.write(image, "png", new File("noise.png"));
	}
}