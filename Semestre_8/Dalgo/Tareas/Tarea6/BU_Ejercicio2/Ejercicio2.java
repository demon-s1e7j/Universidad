// No hace parte de ningun Proyecto

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.lang.Math;
import java.util.Map;
import java.util.Queue;
import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;

class Edge {
  public int toVertex;
  public int flow;
  public int capacity;
  public int reverse;

  public Edge(int toVertex, int flow, int capacity, int reverse) {
    this.toVertex = toVertex;
    this.flow = flow;
    this.capacity = capacity;
    this.reverse = reverse;
  }
  public void show() {
    System.out.printf("vertex: %d, flow: %d, capacity: %d, reverse: %d\n", toVertex, flow, capacity, reverse);
  }
}

class Graph {
  private int V;
  private Map<Integer, Integer> level;
  private Map<Integer, List<Edge>> adj;

  public Graph(Integer[] v) {
    this.adj = new HashMap<Integer, List<Edge>>();
    this.level = new HashMap<Integer, Integer>();
    for (Integer i : v) {
      this.adj.put(i, new ArrayList<Edge>());
      this.level.put(i, -1);
    }
    this.V = v.length;
  }

  public void addEdge(Integer u, Integer v, Integer C) {
    Edge a = new Edge(v, 0, C, adj.get(v).size());
    Edge b = new Edge(u, 0, 0, adj.get(u).size());
    adj.get(u).add(a);
    adj.get(v).add(b);
  }

  public boolean BFS(Integer s, Integer t) {
    for (Integer i = 0; i < V; i++) {
      level.put(i, -1);
    }
    level.put(s, 0);

    Queue<Integer> q = new LinkedList<Integer>();
    q.add(s);

    ListIterator<Edge> i;
    while (q.size() != 0) {
      int u = q.poll();

      for (i = adj.get(u).listIterator(); i.hasNext();) {
        Edge e = i.next();
        if (level.get(e.toVertex) < 0 && e.flow < e.capacity) {
          level.put(e.toVertex, level.get(u) + 1);
          q.add(e.toVertex);
        }
      }
    }

    return level.get(t) > 0;
  }

  public int sendFlow(int u, int flow, int t, int start[]) {
    if (u == t) {
      return flow;
    }

    // Traverse all adjacent edges one -by - one.
    for (; start[u] < adj.get(u).size(); start[u + 2]++) {

      // Pick next edge from adjacency list of u
      Edge e = adj.get(u).get(start[u + 2]);

      if (level.get(e.toVertex) == level.get(u) + 1 && e.flow < e.capacity) {
        // find minimum flow from u to t
        int curr_flow = Math.min(flow, e.capacity - e.flow);

        int temp_flow = sendFlow(e.toVertex, curr_flow, t, start);

        // flow is greater than zero
        if (temp_flow > 0) {
          // add flow  to current edge
          e.flow += temp_flow;

          // subtract flow from reverse edge
          // of current edge
          adj.get(e.toVertex).get(e.reverse).flow -= temp_flow;
          return temp_flow;
        }
      }
    }

    return 0;
  }

  public int maxFlow(int s, int t) {
    if (s == t) {
      return -1;
    }
    int total = 0;
    while(BFS(s, t)) {
      System.out.println(V);
      int[] start = new int[V + 4];

      int flow = -1;
      while (flow != 0) {
        flow = sendFlow(s, Integer.MAX_VALUE, t, start);
        total += flow;
      }
    }
    return total;
  }
}

public class Ejercicio2 {
  //   public static void main(String[] args) {
  //     try (
  //     InputStreamReader is= new InputStreamReader(System.in);
  //     BufferedReader br = new BufferedReader(is); 
  //   ) {
  //       String line = br.readLine();
  //       int[] rnodos = Arrays.stream(line.split(","))
  //       .mapToInt(i -> Integer.parseInt(i))
  //       .toArray();
  //       line = br.readLine();
  //       int[] centros = Arrays.stream(line.split(","))
  //       .mapToInt(i -> Integer.parseInt(i))
  //       .toArray();
  //       line = br.readLine();
  //       int[] tiendas = Arrays.stream(line.split(","))
  //       .mapToInt(i -> Integer.parseInt(i))
  //       .toArray();
  //       Integer[] nodos = new Integer[rnodos.length + 2];
  //       for (int i = 0; i < rnodos.length; i++) {
  //         nodos[i] = rnodos[i];
  //       }
  //       nodos[nodos.length - 2] = Integer.MAX_VALUE - 1;
  //       nodos[nodos.length - 1] = Integer.MAX_VALUE;
  //       Graph g = new Graph(nodos);
  //       Arrays.stream(centros).forEach(f -> {
  //         g.addEdge(Integer.MAX_VALUE - 1, f, Integer.MAX_VALUE);
  //       });
  //       Arrays.stream(tiendas).forEach(f -> {
  //         g.addEdge(f, Integer.MAX_VALUE, Integer.MAX_VALUE);
  //       });

  //       /////////////////////////////////////////////

  //       line = br.readLine();
  //       line = br.readLine();
  //       Map<Integer, Integer> capacidadCentros = new HashMap<Integer, Integer>();
  //       while(!line.contains("transporte")) {
  //         int[] capacidades = Arrays.stream(line.split(","))
  //         .mapToInt(i -> Integer.valueOf(i))
  //         .toArray();
  //         capacidadCentros.put(capacidades[0], capacidades[1]);
  //         line = br.readLine();
  //       }
  //       line = br.readLine();
  //       while (line != null && line.length() > 0) {
  //         int[] values = Arrays.stream(line.split(","))
  //         .mapToInt(i -> Integer.parseInt(i))
  //         .toArray();
  //         Integer C = Math.min(capacidadCentros.getOrDefault(values[0], Integer.MAX_VALUE), capacidadCentros.getOrDefault(values[1], Integer.MAX_VALUE));
  //         C = Math.min(values[2], C);
  //         g.addEdge(values[0], values[1], C);
  //         line = br.readLine();
  //       }
  //       System.out.println("Voy por el flujo maximo");
  //       System.out.println(g.maxFlow(Integer.MAX_VALUE - 1, Integer.MAX_VALUE));
  //     } catch (IOError | IOException e) {
  //       System.err.println("Ocurrio un error" + e.toString());
  //     }
  //   }

  public static void main(String args[]) {
    Graph g = new Graph(new Integer[]{-1, -2, 0, 1, 2, 3, 4, 5});
    g.addEdge(0, 1, 16);
    g.addEdge(0, 2, 13);
    g.addEdge(1, 2, 10);
    g.addEdge(1, 3, 12);
    g.addEdge(2, 1, 4);
    g.addEdge(2, 4, 14);
    g.addEdge(3, 2, 9);
    g.addEdge(3, 5, 20);
    g.addEdge(4, 3, 7);
    g.addEdge(4, 5, 4);
    g.addEdge(-1, 0, Integer.MAX_VALUE);
    // g.addEdge(5, -2, Integer.MAX_VALUE);

    // next exmp
    /*g.addEdge(0, 1, 3 );
        g.addEdge(0, 2, 7 ) ;
        g.addEdge(1, 3, 9);
        g.addEdge(1, 4, 9 );
        g.addEdge(2, 1, 9 );
        g.addEdge(2, 4, 9);
        g.addEdge(2, 5, 4);
        g.addEdge(3, 5, 3);
        g.addEdge(4, 5, 7 );
        g.addEdge(0, 4, 10);

       // next exp
       g.addEdge(0, 1, 10);
       g.addEdge(0, 2, 10);
       g.addEdge(1, 3, 4 );
       g.addEdge(1, 4, 8 );
       g.addEdge(1, 2, 2 );
       g.addEdge(2, 4, 9 );
       g.addEdge(3, 5, 10 );
       g.addEdge(4, 3, 6 );
       g.addEdge(4, 5, 10 ); */

    System.out.println("Maximum flow " + g.maxFlow(0, 5));
  }
}
