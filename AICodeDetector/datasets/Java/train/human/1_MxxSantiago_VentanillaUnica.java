import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Random;

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
    static int ultimo;
    static int ultimoAdultosMayores;
    static Cliente cliente_arribando;
    static Cliente cliente_arribandoAdultosMayores;
    static Cliente cliente_atendiendo;
    static Cliente cliente_atendiendoAdultosMayores;

    public static void main(String[] args) {
        cola = new ArrayDeque<>();
        colaAdultosMayores = new ArrayDeque<>();
        ocupada = false;
        ocupadaAdultosMayores = false;
        atendidos = 0;
        atendidosAdultosMayores = 0;
        espera = 0;
        esperaAdultosMayores = 0;

        Random r = new Random();
        int salida = -1;
        int salidaMayores = -1;

        int llegada = r.nextInt(2) + 3;
        if (r.nextInt(5) == 0) {
            cliente_arribandoAdultosMayores = new Cliente(r.nextInt(60000) + 1, llegada);
            System.out.println("Llegando el adulto mayor " + cliente_arribandoAdultosMayores);
        } else {
            cliente_arribando = new Cliente(r.nextInt(60000) + 1, llegada);
            System.out.println("Llegando el cliente " + cliente_arribando);
        }
        System.out.println("Hora de llegada del primer cliente " + reloj(llegada));

        for (int minuto = 0; minuto <= 600; minuto++) {
            System.out.println(reloj(minuto));
            if (minuto == llegada) {
                if (cliente_arribandoAdultosMayores != null) {
                    System.out.println("Llegando el adulto mayor " + cliente_arribandoAdultosMayores);

                    if (!ocupada && !ocupadaAdultosMayores) {
                        ocupadaAdultosMayores = true;
                        salidaMayores = minuto + r.nextInt(7) + 4;
                        System.out.println("Atendiendo al adulto mayor " + cliente_arribandoAdultosMayores + " en la ventanilla para adultos mayores, saldra en " + (salidaMayores - minuto) + " minutos");
                        cliente_atendiendoAdultosMayores = cliente_arribandoAdultosMayores;
                        ultimoAdultosMayores = minuto - cliente_atendiendoAdultosMayores.getArribo();
                    } else {
                        System.out.println("Ventanilla para adultos mayores ocupada el adulto mayor " + cliente_arribandoAdultosMayores + " se forma en la cola para adultos mayores...");
                        colaAdultosMayores.offer(cliente_arribandoAdultosMayores);
                    }

                    cliente_arribandoAdultosMayores = null;
                } else if (cliente_arribando != null) {
                    System.out.println("Llegando el cliente " + cliente_arribando);

                    if (!ocupada) {
                        ocupada = true;
                        salida = minuto + r.nextInt(7) + 4;
                        System.out.println("Atendiendo al cliente " + cliente_arribando + " en la ventanilla normal, saldra en " + (salida - minuto) + " minutos");
                        cliente_atendiendo = cliente_arribando;
                        ultimo = minuto - cliente_atendiendo.getArribo();
                    } else {
                        System.out.println("Ventanilla normal ocupada el cliente " + cliente_arribando + " se forma en la cola...");
                        cola.offer(cliente_arribando);
                    }
                }

                llegada = minuto + r.nextInt(2) + 3;

                if (r.nextInt(5) == 0) {
                    cliente_arribandoAdultosMayores = new Cliente(r.nextInt(60000) + 1, llegada);
                    cliente_arribando = null;
                    System.out.println("El siguiente cliente es mayor y estara llegando a las: " + reloj(llegada));
                } else {
                    cliente_arribando = new Cliente(r.nextInt(60000) + 1, llegada);
                    cliente_arribandoAdultosMayores = null;
                    System.out.println("El siguiente cliente estara llegando a las: " + reloj(llegada));
                }
            }

            if (minuto == salidaMayores) {
                System.out.println("Termina la atencion del cliente mayor" + cliente_atendiendoAdultosMayores);
                ocupadaAdultosMayores = false;
                atendidosAdultosMayores++;
                if (!colaAdultosMayores.isEmpty()) {
                    cliente_atendiendoAdultosMayores = colaAdultosMayores.poll();
                    int min_arribo = cliente_atendiendoAdultosMayores.getArribo();
                    esperaAdultosMayores = esperaAdultosMayores + (minuto - min_arribo);
                    if ((minuto - min_arribo) != 0) encola++;
                    ocupadaAdultosMayores = true;
                    salidaMayores = minuto + r.nextInt(4) + 2;
                    System.out.println("Atendiendo al cliente mayor " + cliente_atendiendoAdultosMayores + " que estuvo formado " + (minuto - min_arribo) + " minutos y saldra en " + (salida - minuto) + " minutos");
                    ultimoAdultosMayores = minuto - min_arribo;
                }
            }
            if (minuto == salida) {
                System.out.println("Termina la atencion del cliente " + cliente_atendiendo);
                ocupada = false;
                atendidos++;
                if (!cola.isEmpty()) {
                    cliente_atendiendo = cola.poll();
                    int min_arribo = cliente_atendiendo.getArribo();
                    espera = espera + (minuto - min_arribo);
                    if ((minuto - min_arribo) != 0) encola++;
                    ocupada = true;
                    salida = minuto + r.nextInt(4) + 2;
                    System.out.println("Atendiendo al cliente " + cliente_atendiendo + " que estuvo formado " + (minuto - min_arribo) + " minutos y saldra en " + (salida - minuto) + " minutos");
                    ultimo = minuto - min_arribo;
                }
            }
        }

        System.out.println("\n\n");
        System.out.println("Hora de atencion de 8:00 a 18:00");
        System.out.println("Promedio de espera en cola: " + (1.0 * espera / encola) + " minutos");
        System.out.println("Promedio de espera adultos mayores en cola: " + (1.0 * esperaAdultosMayores / encola) + " minutos");
        System.out.println("Cierre de actividades: " + reloj(salida));
        System.out.println("Cierre de actividades adultos mayores: " + reloj(salidaMayores));
        System.out.println("Clientes que se quedaron en espera: " + cola.size());
        System.out.println("Numero de clientes atendidos: " + atendidos);
        System.out.println("Numero de clientes adultos mayores atendidos: " + atendidosAdultosMayores);
        System.out.println("Hora de llegada del ultimo cliente atendido: " + reloj(cliente_atendiendo.getArribo()));
        System.out.println("Hora de llegada del ultimo cliente adulto mayor atendido: " + reloj(cliente_atendiendoAdultosMayores.getArribo()));
        System.out.println("Tiempo de espera del ultimo cliente atendido: " + ultimo);
        System.out.println("Tiempo de espera del ultimo cliente adulto mayor atendido: " + ultimoAdultosMayores);
        System.out.println("Ultimo cliente atendido: " + cliente_atendiendo);
        System.out.println("Ultimo cliente adulto mayor atendido: " + cliente_atendiendoAdultosMayores);

        if (!cola.isEmpty()) {
            System.out.println("Hora de llegada del primer cliente no atendido: " + reloj(cola.peek().getArribo()));
        }
        if (!colaAdultosMayores.isEmpty()) {
            System.out.println("Hora de llegada del primer cliente adulto mayor no atendido: " + reloj(colaAdultosMayores.peek().getArribo()));
        }
    }

    static String reloj(int min) {
        return (8 + (min / 60)) + ":" + ((min % 60 <= 9) ? "0" : "") + (min % 60);
    }
}
