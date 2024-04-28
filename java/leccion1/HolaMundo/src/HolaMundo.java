
import java.util.Scanner;

//primer hola mundo
//comentario en linea
/*comentarios en
varias lineas*/
/*atajo para crear la clase mas rapidamente:
    psvm + tab 
    sout + tab -----> atajo para crear el print mas rapido
     */

public class HolaMundo {

    public static void main(String args[]) {
        //main: metodo de java
        /*System.out.println("Hola Mundo desde Java");

        //el scope de la variable es local, no la puedo usar
        //afuera de este metodo
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;//le asigno otro valor a la variable
        System.out.println(miVariable);//la imprimo en console
        //tipo String: no es primitivo, es un Object
        String miVariableString = "Bienvenidos";
        System.out.println(miVariableString);
        miVariableString = "Sigamos creciendo en programacion";
        System.out.println(miVariableString);*/
        /*reglas para escribir una variable:
        //se debe iniciar con una letra, may o min, pero por 
        convencion se usa camelCase
        No se puede poner un nro al inicio de la variable
        no caracteres especiales
        si _ y si $
        se pueden usar tildes, pero no se recomienda
         */
        /*
        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = usuario + " " + titulo;
        System.out.println("union = " + union);
        
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        //caracteres especiales en Java
        var nombre = "Nuria";
        //salto de linea: \n
        System.out.println("Nueva linea: \n"+nombre);
        //para tabular, espacio dentro de la misma linea: \t
        System.out.println("Tabulador: \t"+nombre);
        System.out.println("\t.:MENU:");
        //caracter de retroceso: borra un lugar hacia atras
        System.out.println("Retroceso: \b"+nombre);
        //comillas simples
        System.out.println("Comillas simples: \'"+nombre+"\'");
        //comillas dobles
        System.out.println("Comillas dobles: \""+nombre+"\"");*/
        
        //Clase Scanner: tiene que ser importada, sino no funciona
        /*
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);
        */
        
        /*
        //Ejercicio con Scanner: Detalles de un libro
        
        Scanner libro = new Scanner(System.in);
        System.out.println("Proporciona el titulo del libro: ");
        String tituloLibro = libro.nextLine();
        System.out.println("Proporciona el autor");
        String autor = libro.nextLine();
        System.out.println("\""+tituloLibro+"\""+" fue escrito por "+autor);
        */
        
        /*
        //tipo entero primitivo: byte
        //cuando le agregamos (byte)delante del nro, obligo a que sea ese 
        //el valor de byte; pero asi tambien se dan errores en la
        //impresion del mismo, ya que se generan imprecisiones
        
        byte numEnteroByte = 127;
        System.out.println("numEnteroByte = "+numEnteroByte);
        System.out.println("Valor minimo del Byte: "+Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: "+Byte.MAX_VALUE);
        
        //Tipo entero primitivo: short
        //si lo obligo a ponerle un nro fuera de sus limites, sucede como
        //con el byte, pueden haber imprecisiones
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = "+numEnteroShort);
        System.out.println("Valor minimo del Short: "+Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: "+Short.MAX_VALUE);
        
        //Tipo entero primitivo: int
        //en el caso del int no se puede forza su limite como en los
        //casos anteriores. Pero puede agregarle un L de long, mas de 
        //32 bytes. Sin embargo, siguen sucediendo las perdidas de precision
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = "+numEnteroInt);
        System.out.println("Valor minimo del int: "+Integer.MIN_VALUE);
        System.out.println("Valor maximo del int: "+Integer.MAX_VALUE);
        
        //Tipo entero primitivo Long
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = "+numEnteroLong);
        System.out.println("Valor minimo del long: "+Long.MIN_VALUE);
        System.out.println("Valor maximo del long: "+Long.MAX_VALUE);
        
        */
        
        //tipo float
        //le tengo que agregar la F al final o definir entre
        //parentesis el tipo  porque por default
        //java toma a los decimales como double
        //float numFloat = (float)10.0;
        float numFloat = 3.4028235E38F;//si necesito un nro mas grande
        //puedo forzarlo con (float), pero lo invalida
        System.out.println("numFloat = "+ numFloat);
        //en console nos lo muestra en formato exponencial.
        //por ej, 1.4E-45
        System.out.println("El valor minimo de float: "+ Float.MIN_VALUE);
        System.out.println("El valor maximo de float: "+ Float.MAX_VALUE);
        
        //tipo double
        //no es necesario poner la D porque por default a los 
        //decimales los toma como double. Sucede lo mismo que en los
        //anteriores con lo de los limites e imprecisiones
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = "+ numDouble);
        System.out.println("El valor minimo de double: "+Double.MIN_VALUE);
        System.out.println("El valor maximo de double: "+Double.MAX_VALUE);
        
        
        
    }   
}
