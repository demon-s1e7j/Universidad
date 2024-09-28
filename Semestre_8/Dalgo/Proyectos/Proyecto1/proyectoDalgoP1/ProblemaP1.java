// Autor: Sergio Montoya Ramirez (S1e7J) - 202112171

import java.util.Arrays; import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.Math;

enum Personaje {
  Marion,
  Indiana,
  Sallah
}

@FunctionalInterface
interface AccesibleOperations {
  boolean isAccesible(int column, int x, int y);
}

public class ProblemaP1 {
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
          int indi = calculate(val, Personaje.Indiana);
          int marion = calculate(val, Personaje.Marion);
          int sallah = calculate(val, Personaje.Sallah);
          System.out.println(indi + marion + sallah);
        } catch (Error | Exception e) {
          System.err.println("Ocurrio un error " + e);
        }
      }
    } catch (IOError | IOException e) {
      System.err.println("Ocurrio un error" + e.toString());
    }
  }

  // Funciones Auxiliares

  public static int getMid(int x) {
    if (x % 2 == 0)
      return x / 2;
    return (x + 1)/2;
  }

  public static boolean[] getCeldasConInfluenciaUp(AccesibleOperations function,
    int columnas, 
    int filas, 
    int x, 
    int y) {
    boolean[] res = new boolean[] {false, false, false};
    for (int i = -1; i < 2; i++) {
      int pos_x = x - 1;
      int pos_y = y + i;
      res[i + 1] = pos_x >= 0 && pos_x < columnas;
      res[i + 1] = res[i + 1] && pos_y >= 0 && pos_y < filas;
      res[i + 1] = res[i + 1] && function.isAccesible(columnas, pos_x, pos_y);
    }

    return res;
  }

  public static boolean[] getCeldasConInfluenciaDown(AccesibleOperations function,
    int columnas,
    int filas,
    int to,
    int x,
    int y) {
    boolean[] res = new boolean[] {false, false, false};
    for (int i = -1; i < 2; i++) {
      int pos_x = x + 1;
      int pos_y = y + i;
      res[i + 1] = pos_x >= 0 && pos_x <= filas;
      res[i + 1] = res[i + 1] && pos_y >= 0 && pos_y <= columnas;
      res[i + 1] = res[i + 1] && function.isAccesible(columnas, pos_x, pos_y);
    }

    return res;
  }

  public static int removeBestWayDown(int[][] val, int[][] matrix, AccesibleOperations function) {
    int max = Arrays.stream(val[val.length - 1]).max().orElse(0);
    return max;
  }

  public static int removeBestWayUp(int[][] val, int[][] matrix, AccesibleOperations function) {
    int l = matrix.length;
    int c = matrix[0].length;

    int max = 0;
    int a_max_x = val.length - 1;

    int a_max_y = 0;
    while (max <= 0 && a_max_x > 0) {
      for (int i = 0; i < val[a_max_x].length; i++) {
        if (max < val[a_max_x][i]) {
          a_max_y = i;
          max = val[a_max_x][a_max_y];
        }
      }

      if (max <= 0)
        a_max_x--;
    }

    for (int i = a_max_x; i > 0; i-- ) {
      matrix[a_max_x][a_max_y] = 0;
      boolean[] pValues = getCeldasConInfluenciaUp(function, l, c, a_max_x, a_max_y);
      a_max_x--;
      int max_y = a_max_y;
      int a_max = 0;
      for (int j = 0; j < 3; j++ ) {
        if (pValues[j] && val[a_max_x][a_max_y + j - 1] > a_max) {
          max_y = a_max_y + j - 1;
          a_max = val[a_max_x][max_y];
        }
      }
      a_max_y = max_y;
    }
    
    return max;
  }
  // Calculos

  public static int calculate(int[][] matrix, Personaje p) {
    int l = matrix.length;
    int c = matrix[0].length;
    int mid_l = getMid(l);
    switch (p) {
      case Indiana:
        return calculateUp(matrix, l,c, mid_l, (int column, int x, int y) -> x >= y);
      case Marion:
        return calculateUp(matrix, l,c, mid_l, (int column, int x, int y) -> x >= (column - y - 1));
      case Sallah:
        return calculateDown(matrix, l, c, mid_l, (int column, int x, int y) -> Math.abs(y - column/2) <= Math.abs(x - l));
    }
    return 2;
  }

  public static int calculateDown(int[][]matrix, int lines, int column, int to, AccesibleOperations function) {

    int[][] val = new int[to][column];

    for (int tx = lines; tx >= to; tx--) {
      for (int ty = 0; ty < column; ty ++) {
        int x = lines - tx;
        int y = ty;
        if (function.isAccesible(column, tx, ty)) {
          boolean[] values = getCeldasConInfluenciaDown(function, column, lines, to, tx, ty);
          int max = 0;
          int nMaldicion = 0;
          for (int i = 0; i < 3; i++) {
            if (values[i]) {
              if (val[x - 1][y + i - 1] > max) {
                max = val[x - 1][y + i - 1];
              }
              if (x - 1 > 0 && val[x - 1][y + i - 1] == -1) {
                nMaldicion++;
              }
            } else if (x - 1 > 0) {
              nMaldicion++;
            }
          }
          val[x][y] = max + matrix[tx - 1][ty];
          if (nMaldicion >= 3) {
            val[x][y] = -1;
          }
          if (matrix[tx - 1][ty] == -1){
            val[x][y] = -1;
          }
        }
        else 
        val[x][y] = 0;
      }
    }
    return removeBestWayDown(val, matrix, function);
  }
  

  public static int calculateUp(int[][]matrix, int lines, int column, int to, AccesibleOperations function) {

    int[][] val = new int[to][column]; // C1 | 1

    for (int x = 0; x < to; x++) { // C2 | n/2
      for (int y = 0; y < column; y++){ // C3 | n/2 * m
        if (function.isAccesible(column, x, y)) { // C4 | n/2 * m
          boolean[] values = getCeldasConInfluenciaUp(function, column, lines, x, y); // O(1) | a
          int max = 0; // C5 | a
          int nMaldicion = 0; // C6 | a
          for (int i = 0; i < 3; i++) { // C7 | 3*a
            if (values[i]) { // C8 | 3*a
              if (val[x - 1][y + i - 1] > max) { // C9 | 3*a
                max = val[x - 1][y + i - 1]; // C10 | 3*a
              }
              if (x - 1 > 0 && val[x - 1][y + i - 1] == -1) { // C11 | 3*a
                nMaldicion++;
              }
            } else if (x - 1 > 0) { // C12 | 3*a
              nMaldicion++;
            }
          }

          val[x][y] = max + matrix[x][y]; // C13 | a

          if (nMaldicion >= 3) { // C14 | a
            val[x][y] = -1; 
          }
          if (matrix[x][y] == -1) { // C15 | a
            val[x][y] = -1;
          }
        }
        else 
        val[x][y] = 0; // C16 | m - a
      }
    }
    return removeBestWayUp(val, matrix, function); // O(n) | 1
  }

  // Conseguir la matriz

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

  // Funciones Auxiliares, Sirven para imprimir matrices para hacer TEST.
  // No deberian usarse en la respuesta final.

  public static void printMatrix(int[][] matrix) {
    for (int[] val: matrix) {
      for (int v: val) {
        System.out.print(v + "| ");
      }
      System.out.println();
    }
  }

  public static void printMatrixAcces(int[][] matrix, AccesibleOperations function) {
    for (int i = 0; i < matrix.length; i++) {
      System.out.print("[ ");
      for (int j = 0; j < matrix[0].length; j++) {
        if (function.isAccesible(matrix[0].length, i, j))
          System.out.print("*, ");
        else
          System.out.print(matrix[i][j] + ", ");
      }
      System.out.println(" ]");
    }
  }
}
