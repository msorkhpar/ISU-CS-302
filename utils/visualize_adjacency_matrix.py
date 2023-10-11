import sys
from typing import List

import networkx as nx
from matplotlib import pyplot as plt


def visualize_adj_matrix(adjacency_matrix: List[List[int]], node_type: str, directed: bool = True):
    if directed:
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()
    num_nodes = len(adjacency_matrix)
    if node_type == "int":
        graph.add_nodes_from(range(num_nodes))
    else:
        graph.add_nodes_from([chr(65 + i) for i in range(num_nodes)])

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                continue
            weight = adjacency_matrix[i][j]
            if weight != sys.maxsize:
                if node_type == "int":
                    graph.add_edge(i, j, weight=weight)
                else:
                    graph.add_edge(chr(65 + i), chr(65 + j), weight=weight)

    pos = nx.spring_layout(graph)

    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=15)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.axis('off')
    plt.show()
