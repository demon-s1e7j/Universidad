// No hace parte de ningun proyecto
// Parti desde la implementación de MergeSort de GFG que se puede encontrar aqui: https://www.geeksforgeeks.org/merge-sort/

import java.io.IOError;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class punto2 {
  public static void main(String[] args) {
		try ( 
			InputStreamReader is= new InputStreamReader(System.in);
			BufferedReader br = new BufferedReader(is);
		) { 
			String line = br.readLine();
			int casos = Integer.parseInt(line);
			line = br.readLine();
			for(int i=0;i<casos && line!=null && line.length()>0;i++) {
				final String [] dataStr = line.split(" ");
				final int[] numeros = Arrays.stream(dataStr).mapToInt(f->Integer.parseInt(f)).toArray();
        sort(numeros);
				line = br.readLine();
			}
		} catch (IOException | IOError e) {
      System.err.println("Ocurrio un error leyendo STDIN");
    }
  }


  public static void sort(int[] a) {
    int[] aux = new int[a.length];
    for (int i = 0; i < a.length; i ++) aux[i] = a[i];
    sort(a, aux, 0, a.length);
    show(aux);
  }

  public static void sort(int[] a, int[] aux, int lo, int hi) {
    // Base
    if (hi - lo < 2) return;
    int tird = lo + (hi - lo)/3;
    int stird = lo + 2 * ((hi - lo)/3) + 1;
    // Divide
    sort(aux, a, tird, stird);
    sort(aux, a, lo  , tird);
    sort(aux, a, stird, hi);
    // Conquer
    merge(aux, a, lo, tird, stird, hi);
  }

  public static void merge(int[] a, int[] aux, int lo, int tird, int stird, int hi) {
    int i = lo, j = tird, k = stird, l = lo;
    while ((i < tird) && (j < stird) && (k < hi)) {
      switch (punto2.min(aux[i], aux[j], aux[k])) {
        case 1: a[l++] = aux[i++];  break;
        case 2: a[l++] = aux[j++];  break;
        case 3: a[l++] = aux[k++];  break;
      }
    }
    while (i < tird && j < stird) {
      switch (punto2.min(aux[i], aux[j])) {
        case 1: a[l++] = aux[i++];  break;
        case 2: a[l++] = aux[j++];  break;
      }
    }
    while (j < stird && k < hi) {
      switch (punto2.min(aux[j], aux[k])) {
        case 1: a[l++] = aux[j++];  break;
        case 2: a[l++] = aux[k++];  break;
      }
    }
    while (i < tird && k < hi) {
      switch (punto2.min(aux[i], aux[k])) {
        case 1: a[l++] = aux[i++];  break;
        case 2: a[l++] = aux[k++];  break;
      }
    }
    while (i < tird) a[l++] = aux[i++];
    while (j < stird) a[l++] = aux[j++];
    while (k < hi) a[l++] = aux[k++];
  }

  public static int min(int a, int b, int c) {
    int val = 0;
    if (a < b) {
      if (a < c) val = 1;
      else val = 3;
    } else {
      if (b < c) val = 2;
      else val = 3;
    }
    return val;
  }
  public static int min(int a, int b) {
    int val = 0;
    if (a <= b) val = 1;
    if (b <= a) val = 2;
    return val;
  }

  public static void show(int[] a) {
    for (int i = 0; i < a.length - 1; i++) System.out.print(a[i] + " ");
    System.out.println(a[a.length - 1]);
  }
}
