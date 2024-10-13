// No pertenece a ningun proyecto

import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Map;
import java.util.Queue;
import java.lang.Math;
import java.io.BufferedReader; 
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ejercicio1 {
  private static final Map<Punto, List<DistanciaPuntos>> grafo = 
  new HashMap<Punto, List<DistanciaPuntos>>();
  private static int tamano;
  public static void main(String[] args) {
    try (
    InputStreamReader is = new InputStreamReader(System.in);
    BufferedReader br = new BufferedReader(is);
    ) {
      String line = br.readLine();
      tamano = Integer.parseInt(line);
      line = br.readLine();
      // INICIO
      int[] arrInicio = Arrays.stream(line.split(" "))
      .mapToInt(c -> Integer.parseInt(c))
      .toArray();
      Punto Inicio = new Punto(arrInicio[0] - 1, arrInicio[1] - 1);
      // Final
      line = br.readLine();
      int[] arrFin = Arrays.stream(line.split(" "))
      .mapToInt(c -> Integer.parseInt(c))
      .toArray();
      Punto Fin = new Punto(arrFin[0] - 1, arrFin[1] - 1);
      // Creando Grafo
      line = br.readLine();
      for (int i = 0; i < tamano && line != null && line.length() > 0; i++) {
        for (int j = 0; j < tamano; j++) {
          char val = line.charAt(j);
          if (val == '0') {
            Punto p = new Punto(i, j);
            if (p.equals(Inicio)) {
              Inicio = p;
            }
            if (p.equals(Fin)) {
              Fin = p;
            }
            agregarPunto(p);
          }
        }
        line = br.readLine();
      }
      int valor = analizar(Inicio, Fin);
      System.out.println(valor);
    } catch (IOError | IOException e) {
      System.err.println("Ocurrio un error " + e.toString());
    }
  }

  public static List<Punto> conseguirCamino0(Punto p) {
    List<Punto> caminos_0 = new LinkedList<Punto>();
    Queue<Punto> queue = new LinkedList<Punto>();
    for (DistanciaPuntos d : grafo.get(p)) {
      if (d.distancia == 0.0) {
        queue.add(d.p);
        caminos_0.add(d.p);
      }
    }
    Punto val = queue.poll();
    while (val != null) {
      for (DistanciaPuntos d: grafo.get(val)) {
        if (d.distancia == 0.0 && !caminos_0.contains(d.p)) {
          queue.add(d.p);
          caminos_0.add(d.p);
        }
      }
      val = queue.poll();
    }
    return caminos_0;
  }

  public static int analizar(Punto i, Punto f) {
    List<Punto> caminos0I = conseguirCamino0(i);
    List<Punto> caminos0F = conseguirCamino0(f);
    double puente = encontrarMejorPuente(caminos0I, caminos0F);
    return (int)puente;
  }

  public static double encontrarMejorPuente(List<Punto> c0i, List<Punto> c0f) {
    double min = (double)3*tamano*tamano;
    for (Punto p: c0i) {
      for (DistanciaPuntos d: grafo.get(p)) {
        if (c0f.contains(d.p) && d.distancia < min) {
          min = d.distancia;
        }
      }
    }
    return min;
  }

  public static void agregarPunto(Punto p) {
    if (grafo.get(p) == null) {
      grafo.put(p, new LinkedList<DistanciaPuntos>());
    }
    for (Punto punto : grafo.keySet()) {
      DistanciaPuntos distancia = new DistanciaPuntos(p, punto);
      grafo.get(punto).add(distancia);
      if (p != punto) {
        grafo.get(p).add(new DistanciaPuntos(punto, distancia.distancia));
      }
    }
  }
}

class Punto {
  int f;
  int c;

  public Punto(int f, int c) {
    this.f = f;
    this.c = c;
  }

  public int getF() {
    return this.f;
  }

  public int getC() {
    return this.c;
  }

  public void mostrarCoordenadas() {
    System.out.printf("El punto esta en f: %d, c: %d\n", this.f, this.c);
  }

  public boolean equals(Punto p) {
    return this.f == p.f && this.c == p.c;
  }
}

class DistanciaPuntos {
  Punto p; 
  double distancia;

  public DistanciaPuntos(Punto pPropio, Punto pObjetivo) {
    this.p = pPropio;
    if (pPropio.getF() == pObjetivo.getF() && Math.abs(pPropio.getC() - pObjetivo.getC()) <= 1) {
      this.distancia = 0.0;
    } else if (pPropio.getC() == pObjetivo.getC() && Math.abs(pPropio.getF() - pObjetivo.getF()) <= 1){
      this.distancia = 0.0;
    } else {
      this.distancia = Math.pow(pPropio.getF() - pObjetivo.getF(), 2)
      + Math.pow(pPropio.getC() - pObjetivo.getC(), 2);
    }
  }

  public DistanciaPuntos(Punto p, double distancia) {
    this.p = p;
    this.distancia = distancia;
  }

  public void show() {
    System.out.printf("El punto %d, %d esta a %f\n", p.getF(), p.getC(), distancia);
  }
}
