// No esta en ningun proyecto

import java.util.Arrays;
import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;

public class proyecto1 {
  public static void main(String[] args) {
    try (
    InputStreamReader is= new InputStreamReader(System.in);
    BufferedReader br = new BufferedReader(is); 
  ) {
      String line = br.readLine();
      int casos = Integer.parseInt(line);
      for (int i = 0; i<casos && line != null && line.length() > 0; i++) {
        try {
          int[][] val = getMatrix(br);
          System.out.println("***********************************************");
          printMatrix(val);
        } catch (Error | Exception e) {
          System.err.println("Ocurrio un error " + e);
        }
      }
    } catch (IOError | IOException e) {
      System.err.println("Ocurrio un error" + e.toString());
    }
  }
  public static int[][] getMatrix(BufferedReader br) throws Exception, Error {
    try {
      String line = br.readLine();
      int[] cases = Arrays.stream(line.split(" "))
        .mapToInt(f -> Integer.parseInt(f))
        .toArray();
      int[][] matrix = new int[cases[0]][cases[1]];
      for (int i = 0; i<cases[0] && line != null && line.length() > 0; i++) {
        line = br.readLine();
        matrix[i] = Arrays.stream(line.split(" "))
          .mapToInt(f -> Integer.parseInt(f))
          .toArray();
      }
      return matrix;
    } catch (Error | Exception e) {
      throw e;
    }
  }

  public static void printMatrix(int[][] matrix) {
    for (int[] val: matrix) {
      System.out.print("[ ");
      for (int v: val) {
        System.out.print(v + ", ");
      }
      System.out.println(" ]");
    }
  }
}
