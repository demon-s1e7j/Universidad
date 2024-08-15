import java.util.Arrays;
import java.lang.Math;
import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;

public class PrimeraTarea {
  public static void main(String[] args) {
    try (
      InputStreamReader is= new InputStreamReader(System.in);
      BufferedReader br = new BufferedReader(is); 
      ) {
      String line = br.readLine();
      int casos = Integer.parseInt(line);
      line = br.readLine();
      for (int i = 0; i<casos && line != null && line.length() > 0; i++) {
        int[] valores = Arrays.stream(line.split(" ")).mapToInt(f -> Integer.parseInt(f)).toArray();
        PrimeraTarea.desarrollo(valores);
        line = br.readLine();
      }
    } catch (IOError | IOException e) {
      System.err.println("Ocurrio un error" + e.toString());
    }
  }

  public static void desarrollo(int[] valores) {
    double promedio = PrimeraTarea.calcularMedia(valores);
    double desviacionEstandarPoblacional = 
    PrimeraTarea.calcularDesviacionEstandarPoblacional(valores, promedio);
    PrimeraTarea.imprimirValores(promedio, desviacionEstandarPoblacional);
  }

  public static double calcularMedia(int[] valores) {
    return Arrays.stream(valores).sum()/valores.length;
  }

  public static double calcularDesviacionEstandarPoblacional(int[] valores, double promedio) {
    double suma_corregida = Arrays.stream(valores).mapToDouble(x -> Math.pow((x - promedio), 2)).sum();
    return Math.sqrt(suma_corregida/valores.length);
  }

  public static double truncateDouble(double val) {
    return Math.floor(val * 100) / 100;
  }

  public static void imprimirValores(double promedio, double desviacionEstandarPoblacional) {
    System.out.format("%.2f",truncateDouble(promedio));
    System.out.print(" ");
    System.out.format("%.2f\n",truncateDouble(desviacionEstandarPoblacional));
  }
}
