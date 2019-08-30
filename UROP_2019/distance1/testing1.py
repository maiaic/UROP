import graph_that
from actions import to_graph

data_points = to_graph()

for pair in data_points.keys():
    graph_that.lets_do_a_graph(pair)

