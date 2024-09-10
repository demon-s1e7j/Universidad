// No hace parte de un projecto

import java.util.Arrays;
import java.lang.Math;
import java.io.BufferedReader;
import java.io.IOError; import java.io.IOException;
import java.io.InputStreamReader;

public class pregunta2 {
  public static void main(String[] args) {
    try (
    InputStreamReader is= new InputStreamReader(System.in);
    BufferedReader br = new BufferedReader(is); 
  ) {
      String line = br.readLine();
      int casos = Integer.parseInt(line);
      boolean[] res = new boolean[casos];
      line = br.readLine();
      for (int i = 0; i < casos && line != null && line.length() > 0; i++) {
        int[] nums = Arrays.stream(line.split(" ")).mapToInt(f -> Integer.parseInt(f)).toArray();
        boolean isDiv = pregunta2.isDividible(nums);
        res[i] = isDiv;
        line = br.readLine();
      }
      for (boolean var : res) {
        System.out.println(var);
      }
    } catch (IOError | IOException e) {
      System.err.println("Ocurrio un error" + e.toString());
    }
  }

  public static boolean isDividible(int[] arr) {
    int sum = Arrays.stream(arr).sum();

    if (sum % 2 != 0)
    return false;

    sum = sum / 2;

    boolean[][] matrix = new boolean[arr.length + 1][sum + 1];

    for (int i = 0; i < sum + 1; i++)
    matrix[0][i] = false;

    for (int i = 0; i < arr.length + 1; i++)
    matrix[i][0] = true;

    for (int i = 1; i < arr.length + 1; i++) {
      for (int j = 1; j < sum + 1; j++) {

        if(j < arr[i-1])
        matrix[i][j] = matrix[i-1][j] ; 

        else
        matrix[i][j] = matrix[i-1][j] || matrix[i-1][j-arr[i-1]] ; 
      }
    }
    return matrix[arr.length][sum];
  }

  public static void imprimirMatriz(boolean[][] matrix) {
    for (boolean[] a: matrix) {
      for (boolean b: a) 
      System.out.print(b + " ");
      System.out.println();
    }
  }

  public static void imprimirArray(int[] arr) {
    System.out.print("[");
    Arrays.stream(arr).forEach(f -> System.out.print(f + " "));
    System.out.println("]");
  }
}
