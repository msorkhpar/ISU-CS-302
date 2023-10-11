import sys
from typing import List

from utils.loader import load_base_configs
from utils.graph_constructor import load_graph_from_file
from utils.visualize_adjacency_matrix import visualize_adj_matrix


def find_path(p, u, node_type):
    to = u if node_type == "int" else chr(65 + u)
    if u == 0:
        print(to, end=" ")
        return
    find_path(p, p[u], node_type)
    print(to, end=" ")


def shortest_path(graph: List[List[int]], node_type: str):
    node_size = len(graph)

    distance_table = [sys.maxsize] * node_size
    path = [0] * node_size
    visited = [0] * node_size

    for i in range(1, node_size):
        distance_table[i] = graph[0][i]

    visited[0] = 1
    distance_table[0] = 0

    for i in range(1, node_size):
        min_val = sys.maxsize
        smallest = None

        for j in range(1, node_size):
            if visited[j] == 0 and distance_table[j] < min_val:
                min_val = distance_table[j]
                smallest = j

        if smallest is not None:
            visited[smallest] = 1
            for j in range(1, node_size):
                if visited[j] == 0 and distance_table[j] > (distance_table[smallest] + graph[smallest][j]):
                    distance_table[j] = distance_table[smallest] + graph[smallest][j]
                    path[j] = smallest

    for i in range(1, node_size):
        start = 0 if node_type == "int" else "A"
        to = i if node_type == "int" else chr(65 + i)
        if distance_table[i] == sys.maxsize:
            print(f"No path from {start} to {to}")
            continue

        print(f"Shortest path from {start} to {to} is {distance_table[i]}")
        find_path(path, i, node_type)
        print()


if __name__ == '__main__':
    env, logger = load_base_configs()
    edge_list_path = env.str('EDGE_LIST_PATH')
    node_type = env.str('NODE_TYPE')
    adjacency_matrix = load_graph_from_file(edge_list_path, node_type)
    visualize_adj_matrix(adjacency_matrix, node_type)
    shortest_path(adjacency_matrix, node_type)
