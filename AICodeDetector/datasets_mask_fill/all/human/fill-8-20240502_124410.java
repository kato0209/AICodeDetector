import java.util.ArrayDeque;
import java.util.Queue;
import apropia.Cliente;

public class VentanillaUnica {
   static Queue<Cliente> cola;
    static Queue<Cliente> colaAdultosMayores;
    static boolean ocupada;
    static boolean ocupadaAdultosMayores;
   static int atendidos;
    static int atendidosAdultosMayores;
    static int encola;
    static int espera;
    static int esperaAdultosMayores;
 static int   ultimo;
    static int ultimoAdultosMayores;
    static Cliente cliente_arribando;
    static Cliente cliente_arribandoAdultosMayores;
    static Cliente cliente_atendiendo;
    static Cliente cliente_atendiendoAdultosMayores;

   public static void main(String[] args) {
        cola = new ArrayDeque<>();
       colaAdultosMayores = new ArrayDeque<>();
