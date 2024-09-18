// No hace parte de ningun proyecto

import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class proyecto1 {
  public static void main(String[] args) {
    try (
    InputStreamReader is= new InputStreamReader(System.in);
    BufferedReader br = new BufferedReader(is);
  ) {
      String line = br.readLine();
      int casos = Integer.parseInt(line);
      for (int i = 0; i<casos && line != null && line.length() > 0; i++) {
        getMatriz(br);
      }
    } catch (IOError | IOException e) {
      System.err.println("Ocurrio un error" + e.toString());
    }

  }

  public static int[][] getMatriz(BufferedReader br) {
    try {
      String line = br.readLine();
      int[] size = Arrays.stream(line.split(" ")).mapToInt(s -> Integer.parseInt(s)).toArray();
      int[][] vals = new int[size[0]][size[1]];
      for (int i = 0; i < size[0] && line != null && line.length() > 0; i++) {
        line = br.readLine();
        vals[i] = Arrays.stream(line.split(" ")).mapToInt(x -> Integer.parseInt(x)).toArray();
      }
      Arrays.stream(vals).forEach(
        a -> {
          Arrays.stream(a).forEach(i -> System.out.print(i));
          System.out.println();
        }
      );
    } catch (IOError | IOException e) {
      System.err.println("Ocurrio un error" + e.toString());
    }
    return new int[][] {new int[] {1, 2}};
  }
}
