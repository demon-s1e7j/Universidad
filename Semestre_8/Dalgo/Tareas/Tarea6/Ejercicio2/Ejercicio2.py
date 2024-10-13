# Por honestidad debo decir que la implementación de FordFulkerson viene
# de lo hablado en clase y de buscar este algoritmo 
# (Pues sabia de antemano que ya existia) y por que gaste mucho tiempo
# intentando implementarlo en Java (pueden pedirme este codigo, que no funciona)
# lamento los inconvenientes

import sys

class Graph:
	def __init__(self, graph):
		self.graph = graph
		self. ROW = len(graph)
		# self.COL = len(gr[0])

	def BFS(self, s, t, parent):

		visited = [False]*(self.ROW)

		queue = []

		queue.append(s)
		visited[s] = True

		while queue:
			u = queue.pop(0)
			for ind, val in enumerate(self.graph[u]):
				if not visited[ind] and val > 0:
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u
					if ind == t:
						return True
		return False
			
	
	def FordFulkerson(self, source, sink):
		parent = [-1]*(self.ROW)
		max_flow = 0
		while self.BFS(source, sink, parent) :
			path_flow = float("Inf")
			s = sink
			while(s != source):
				path_flow = min (path_flow, self.graph[parent[s]][s])
				s = parent[s]
			max_flow += path_flow
			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]
		return max_flow


locations = list(map(int, sys.stdin.readline().split(",")))

beg = locations[0]

source = locations[len(locations) - 1] + 1
sink = locations[len(locations) - 1] + 2

locations.extend([source, sink])

graph = []
for x in locations:
    line = []
    for y in locations:
        line.append(0)
    graph.append(line)

for centro in list(map(int, sys.stdin.readline().split(","))):
    graph[-2][centro - beg] = sys.maxsize

for tienda in list(map(int, sys.stdin.readline().split(","))):
    graph[tienda - beg][-1] = sys.maxsize

sys.stdin.readline()
line = sys.stdin.readline()

capacidades = {}
while "transporte" not in line:
    c = list(map(int, line.split(",")))
    capacidades[c[0]] = c[1]
    line = sys.stdin.readline()

line = sys.stdin.readline()
while len(line) > 0 and line is not None:
    v = list(map(int, line.split(",")))
    capacidad = min(v[2],
                    capacidades.get(v[0], sys.maxsize),
                    capacidades.get(v[1], sys.maxsize))
    graph[v[0] - beg][v[1] - beg] = capacidad
    line = sys.stdin.readline()

g = Graph(graph)

print(g.FordFulkerson(len(graph) - 2, len(graph) - 1))
