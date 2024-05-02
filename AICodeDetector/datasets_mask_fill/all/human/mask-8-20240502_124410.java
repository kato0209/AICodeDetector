import java.util.ArrayDeque;
import java.util.Queue;
import <extra_id_0> VentanillaUnica {
 <extra_id_1>  static Queue<Cliente> cola;
    static Queue<Cliente> colaAdultosMayores;
    static boolean ocupada;
    static boolean ocupadaAdultosMayores;
  <extra_id_2> static int atendidos;
    static int atendidosAdultosMayores;
    static int encola;
    static int espera;
    <extra_id_3> esperaAdultosMayores;
 <extra_id_4>  <extra_id_5> ultimo;
    <extra_id_6> ultimoAdultosMayores;
    static Cliente cliente_arribando;
    static Cliente cliente_arribandoAdultosMayores;
    static Cliente cliente_atendiendo;
    static Cliente cliente_atendiendoAdultosMayores;

  <extra_id_7> public static void main(String[] args) {
        cola = new ArrayDeque<>();
     <extra_id_8>  colaAdultosMayores = new ArrayDeque<>();
