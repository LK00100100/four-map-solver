# solves the 4-map game on Mobaxterm
# python 3.7
# author lk00100100
from FourMapSolver import FourMapSolver
from GraphReader import GraphReader

filename = 'samples/graph1.txt'

graph = GraphReader.read_graph(filename)

solver = FourMapSolver()

#solved_graph = solver.solve(graph)

for node_id in graph:
    node = graph[node_id]
    print(node)
