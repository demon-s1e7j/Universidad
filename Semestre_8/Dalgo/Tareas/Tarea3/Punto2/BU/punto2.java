// No hace parte de ningun proyecto

import java.util.Arrays;

public class punto2 {
  public static void main(String[] args) {
    int[] data = new int[] {45, -2, -45, 78, 30, -42, 10, 19, 73, 93};
    sort(data);
  }


  public static void sort(int[] a) {
    int[] aux = new int[a.length];
    sort(a, aux, 0, a.length - 1);
    show(a);
  }

  public static void sort(int[] a, int[] aux, int lo, int hi) {
    // Base
    if (hi <= lo) return;
    int tird = lo + (hi - lo)/3;
    int stird = lo + 2 * ((hi - lo)/3);
    System.out.printf("Entro a la función Sort con los valores: lo:%d tird:%d stird:%d hi:%d\n", lo, tird, stird, hi);
    show(a);
    // Divide
    sort(a, aux, lo       , tird);
    sort(a, aux, tird  + 1, stird);
    sort(a, aux, stird + 1, hi   );
    // Conquer
    merge(a, aux, lo, tird, stird, hi);
  }

  public static void merge(int[] a, int[] aux, int lo, int tird, int stird, int hi) {
    System.out.printf("Entro a la función Merge con los valores: lo:%d tird%d s:tird%d hi:%d\n", lo, tird, stird, hi);
    for (int k = lo; k <= hi; k++) {
      aux[k] = a[k];
    }

    int i = lo, j = tird, k = stird;
    int l = lo;
    while ((i < tird) && (j < stird) && (k < hi)) {
      System.out.println("Entro caso 1");
      switch (punto2.min(aux[i], aux[j], aux[k])) {
        case 1: a[l++] = a[i++]; break;
        case 2: a[l++] = a[j++]; break;
        case 3: a[l++] = a[k++]; break;
      }
    }
    while (i < tird && j < stird) {
      System.out.println("Entro caso 2");
      switch (punto2.min(aux[i], aux[j])) {
        case 1: a[l++] = a[i++]; break;
        case 2: a[l++] = a[j++]; break;
      }
    }
    while (j < stird && k < hi) {
      System.out.println("Entro caso 3");
      switch (punto2.min(aux[i], aux[j])) {
        case 1: a[l++] = a[i++]; break;
        case 2: a[l++] = a[j++]; break;
      }
    }
    while (i < tird && k < hi) {
      System.out.println("Entro caso 4");
      switch (punto2.min(aux[i], aux[j])) {
        case 1: a[l++] = a[i++]; break;
        case 2: a[l++] = a[j++]; break;
      }
    }
    while (i < tird) a[l++] = a[i++];
    while (j < stird) a[l++] = a[j++];
    while (k < hi) a[l++] = a[k++];
  }

  public static int min(int a, int b, int c) {
    int val = 0;
    if (a <= b && a <= c) val = 1;
    if (b <= a && b <= c) val = 2;
    if (c <= a && c <= b) val = 3;
    System.out.printf("A:%d, B:%d C:%d - return %d\n", a, b, c, val);
    return val;
  }
  public static int min(int a, int b) {
    int val = 0;
    if (a <= b) val = 1;
    if (b <= a) val = 2;
    System.out.printf("A:%d, B:%d - return %d\n", a, b, val);
    return val;
  }

  public static void show(int[] a) {
    for (int i = 0; i < a.length - 1; i++) System.out.print(a[i] + " ");
    System.out.println(a[a.length - 1]);
  }
}
