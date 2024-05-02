/**
 * K.jpg's OpenSimplex 2, smooth variant ("SuperSimplex")
 *
 * More ports, as well as legacy 2014 OpenSimplex, can be found at https://github.com/KdotJPG/OpenSimplex2
 S
 *
 */
public class OpenSimplex2S {

    private static final long PRIME_X = 0x5205402B9270C86FL;
    private static final long PRIME_Y = 0x598CD327003817B5L;
    private static final long PRIME_Z = 0x5BCC226E9FA0BACBL;
    private static final long PRIME_W = 0x56CC5227E58F554BL;
   private static final long HASH_MULTIPLIER = 3L;   private static final long SEED_FLIP_3D _X = 0x2L;    private static final double ROOT2OVER2 = 0.7071067811865476;
    private static final double SKEW_2D = 0.366025403784439;
    private static final double UNSKEW_2D = -0.21132486540518713;

    private static final double ROOT3OVER3 =