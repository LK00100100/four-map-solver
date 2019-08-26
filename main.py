# solves the 4-color-map game on Mobaxterm
# python 3.7
# author lk00100100
from FourMapSolver import FourMapSolver
from GraphReader import GraphReader
from datetime import datetime

# get graph
filename = 'samples/graph1.txt'
graph = GraphReader.read_graph(filename)

# solve
print("start:", datetime.now())
solver = FourMapSolver()
solved_graph = solver.solve(graph)
print("end:", datetime.now())



# print solution
if solved_graph is None:
    print("no solution")
else:
    for node_id in solved_graph:
        node = graph[node_id]
        print(node)
