// No pertenece a un proyecto

import java.util.Arrays;
import java.util.Comparator;
import java.lang.Math;
import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;

public class pregunta1 {
  public static void main(String[] args) {
    try (
    InputStreamReader is = new InputStreamReader(System.in);
    BufferedReader br = new BufferedReader(is);
    ) {
      String line = br.readLine();
      int casos = Integer.parseInt(line);
      Job[] possibleJobs = new Job[casos];
      line = br.readLine();
      for (int i = 0; i<casos && line != null && line.length() > 0; i++) {
        possibleJobs[i] = new Job(line);
        line = br.readLine();
      }
      Arrays.sort(possibleJobs, new Comparator<Job>() {
        public int compare(Job j1, Job j2) {
          return j1.getEnd() - j2.getEnd();
        }
      });
      int mejor = pregunta1.mejoresTrabajos(possibleJobs);
      System.out.println(mejor);
    } catch (IOError | IOException e) {
      System.err.println("Ocurrio un error " + e);
    }
  }

  public static int noChocan(Job[] possibleJobs, int from) {
    for (int i = from - 1; i > -1; i--){
      if (possibleJobs[i].getEnd() <= possibleJobs[from].getBegin()) {
        return i;
      }
    }
    return -1;
  }

  public static int mejoresTrabajos(Job[] possibleJobs) {
    int[] values = new int[possibleJobs.length + 1];

    values[0] = 0;

    for (int i = 1; i < values.length; i++) {
      int noTomarlo = values[i - 1];
      int Tomarlo = possibleJobs[i - 1].getIncome();
      int noChocan = pregunta1.noChocan(possibleJobs, i - 1);
      if (noChocan > -1)
        Tomarlo = values[noChocan + 1] + Tomarlo;
      values[i] = Integer.max(noTomarlo, Tomarlo);
    }

    return values[values.length - 1];
  }

  public static void imprimirMatriz(int[][] matrix) {
    Arrays.stream(matrix).forEach(f -> {
      Arrays.stream(f).forEach(x -> System.out.print(x));
      System.out.println();
    });
  }
}

class Job {
  int begin;
  int end;
  int income;
  public Job(String str) {
    int[] values = Arrays.stream(str.split(" ")).mapToInt(f -> Integer.parseInt(f)).toArray();
    this.begin = values[0];
    this.end = values[1];
    this.income = values[2];
  }

  public void imprimirTarea() {
    System.out.printf("Esta tarea inicia a las: %d Termina a las: %d y tiene una ganancia de: %d\n"
    , this.begin, this.end, this.income);
  }

  public int getBegin() {
    return this.begin;
  }
  public int getEnd() {
    return this.end;
  }
  public int getIncome() {
    return this.income;
  }
}
