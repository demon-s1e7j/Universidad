// No esta en ningun proyecto.

import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;

public class punto1 {
  public static void main(String[] args) {
    int[][] matrix = punto1.getMatrix();
    int res = maxMatrix(matrix);
    System.out.println(res);
  }

  public static int maxMatrix(int[][] matrix) {
    return maxMatrix(matrix, 0, matrix.length - 1, 0, matrix[0].length - 1);
  }

  public static int maxMatrix(int[][] matrix, int from_x, int to_x, int from_y, int to_y) {
    if (to_x - from_x < 1 && to_y - from_y < 1) return matrix[to_x][to_y];
    int mid_x = from_x + (to_x - from_x)/2;
    mid_x = Math.min(mid_x, to_x - 1);
    int mid_y = from_y + (to_y - from_y)/2;
    mid_y = Math.min(mid_y, to_y - 1);

    int val1 = maxMatrix(matrix, from_x, mid_x, from_y, mid_y);
    int val2 = maxMatrix(matrix, mid_x + 1, to_x, from_y, mid_y);
    int val3 = maxMatrix(matrix, from_x, mid_x, mid_y + 1, to_y);
    int val4 = maxMatrix(matrix, mid_x + 1, to_x, mid_y + 1, to_y);

    return Math.max(Math.max(val1, val2), Math.max(val3, val4));
  }

  public static int[][] getMatrix() {
		try ( 
			InputStreamReader is= new InputStreamReader(System.in);
			BufferedReader br = new BufferedReader(is);
		) { 
			String line = br.readLine();
			int[] valores = Arrays.stream(line.split(" ")).mapToInt(f -> Integer.parseInt(f)).toArray();
      int filas = valores[0];
      int columnas = valores[1];
      int[][] matrix = new int[filas][columnas];
			line = br.readLine();
			for(int i=0;i<filas && line!=null && line.length()>0;i++) {
        valores = Arrays.stream(line.split(" ")).mapToInt(f -> Integer.parseInt(f)).toArray();
        matrix[i] = valores;
				line = br.readLine();
			}
      return matrix;
		}
    catch (IOException | IOError e) {
      System.err.println("Ocurrio un error");
    }
    return null;
  }
}
