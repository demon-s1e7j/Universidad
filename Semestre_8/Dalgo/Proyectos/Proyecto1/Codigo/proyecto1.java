// No esta en ningun proyecto

import java.util.Arrays;
import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.function;

import com.sun.org.apache.xpath.internal.functions.Function;

enum Personaje {
  Indiana,
  Marion,
  Sallah
}

@FunctionalInterface
interface AccesibleOperations {
  boolean isAccesible(int column, int x, int y);
}

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
          printMatrix(val);
          int indi = calculate(matrix);
        } catch (Error | Exception e) {
          System.err.println("Ocurrio un error " + e);
        }
      }
    } catch (IOError | IOException e) {
      System.err.println("Ocurrio un error" + e.toString());
    }
  }

  public static void calculate(int[][] matrix, Personaje p) {
    int l = matrix.length;
    int c = matrix[0].length;
    int mid_l = l / 2;
    int mid_c = c / 2;
  }

  public static void calculate(int[][]matrix, int from, int to, )

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
      for (int v: val) {
        System.out.print(v + "| ");
      }
      System.out.println();
    }
  }

  public static void printMatrixAcces(int[][] matrix) {
    for (int i = 0; i < matrix.length; i++) {
      System.out.print("[ ");
      for (int j = 0; j < matrix[0].length; j++) {
        if (isAccesible(matrix[0].length, i, j))
          System.out.print("*, ");
        else
          System.out.print(matrix[i][j] + ", ");
      }
      System.out.println(" ]");
    }
  }

  public static boolean isAccesible(int column, int x, int y) {
    return x >= y || x >= (column - y - 1);
  }
}
