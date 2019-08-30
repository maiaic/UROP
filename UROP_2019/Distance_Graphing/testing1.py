import graph_that
from actions import to_graph

data_points = to_graph()

for pair in data_points.keys():
    graph_that.graph_distances(pair)

